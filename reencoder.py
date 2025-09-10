# TODO: handle last byte properly

import io
import zlib
from collections import defaultdict
from typing import NamedTuple, Optional, Self

CLEN_ORDER = [16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]


class BitReader:
    def __init__(self, data: bytes):
        self.stream = io.BytesIO(data)
        self.buffer = 0
        self.buffer_size = 0

    def read(self, n: int) -> int:
        while self.buffer_size < n:
            byte = self.stream.read(1)
            self.buffer |= byte[0] << self.buffer_size
            self.buffer_size += 8

        ret = self.buffer & (1 << n) - 1
        self.buffer >>= n
        self.buffer_size -= n

        return ret


class BitString(NamedTuple):
    value: int
    size: int

    def __add__(self, other: Self) -> Self:
        return BitString((other.value << self.size) | self.value, self.size + other.size)

    def to_bytes(self) -> tuple[bytes, Self]:
        data = self.value.to_bytes((self.size >> 3) + 1, "little")
        return data[:-1], BitString(data[-1], self.size & 7)


class Huffman:
    def __init__(self, lit_tree, dist_tree, raw):
        self.lit = lit_tree
        self.dist = dist_tree
        self.raw = raw

    @staticmethod
    def _build_tree(lengths: list[int]) -> dict:
        tree = {}
        code = length = 0
        for sym in sorted(range(len(lengths)), key=lengths.__getitem__):
            if lengths[sym] == 0:
                continue
            code <<= lengths[sym] - length
            length = lengths[sym]
            rev = int(f"{code:0{length}b}"[::-1], 2)
            tree[sym] = BitString(rev, length)
            tree[BitString(rev, length)] = sym
            code += 1
        return tree

    @classmethod
    def parse(cls, deflate: bytes):
        reader = BitReader(deflate)

        final = reader.read(1)
        btype = reader.read(2)

        assert final == 1
        assert btype == 2

        hlit = reader.read(5) + 257
        hdist = reader.read(5) + 1
        hclen = reader.read(4) + 4

        lengths = [0] * len(CLEN_ORDER)
        for sym in CLEN_ORDER[:hclen]:
            lengths[sym] = reader.read(3)
        cl_tree = cls._build_tree(lengths)

        used = 17 + 3 * hclen

        lengths = []
        while len(lengths) < hlit + hdist:
            code = length = 0
            while (code, length) not in cl_tree:
                code = code | (reader.read(1) << length)
                length += 1
            sym = cl_tree[code, length]

            used += length

            if sym < 16:
                lengths.append(sym)
            elif sym == 16:
                lengths.extend(lengths[-1:] * (reader.read(2) + 3))
                used += 2
            elif sym == 17:
                lengths.extend([0] * (reader.read(3) + 3))
                used += 3
            elif sym == 18:
                lengths.extend([0] * (reader.read(7) + 11))
                used += 7

        return cls(
            cls._build_tree(lengths[:hlit]),
            cls._build_tree(lengths[hlit:]),
            BitString(BitReader(deflate).read(used), used),
        )

    def encode_lit(self, x: int) -> Optional[BitString]:
        return self.lit.get(x)

    def encode_len(self, x: int) -> Optional[BitString]:
        start, extra_bits = 3, 0
        for sym in range(257, 285):
            extra_bits += 264 < sym and sym % 4 == 1
            if x < start + (1 << extra_bits):
                code = self.lit.get(sym)
                return code + BitString(x - start, extra_bits) if code else None
            start += 1 << extra_bits

    def encode_dist(self, x: int) -> Optional[BitString]:
        start, extra_bits = 1, 0
        for sym in range(30):
            extra_bits += 3 < sym and sym % 2 == 0
            if x < start + (1 << extra_bits):
                code = self.dist.get(sym)
                return code + BitString(x - start, extra_bits) if code else None
            start += 1 << extra_bits


class State(NamedTuple):
    prev: int  # 0 = regular, 1 = null, 2 = backslash
    value: BitString


def merge(state: State, code: BitString, delim: bytes) -> tuple[State, int]:
    prev = state.prev
    stream, value = (state.value + code).to_bytes()

    cost = code.size

    for byte in stream:
        if prev == 1 and byte in b"01234567":
            cost += 16
        elif prev == 2 and byte in b"\0\n\r01234567abfxnrtvuUN'\"\\":
            cost += 8

        if byte == 0:
            prev = 1
            cost += 8
        elif byte == ord("\r"):
            prev = 0
            cost += 8
        elif byte == ord("\n") and len(delim) == 1:
            prev = 0
            cost += 8
        elif byte == delim[0] and len(delim) == 1:
            prev = 0
            cost += 8
        else:
            prev = 2 if byte == ord("\\") else 0

    return State(prev, value), cost


def lz77(data: bytes, huffman: Huffman, delim: bytes):
    index = defaultdict(list)
    for start in range(len(data)):
        for end in range(start + 3, len(data) + 1):
            index[data[start:end]].append(start)

    refs = [[] for _ in range(len(data) + 1)]
    for substr in index:
        curr = []
        for start in index[substr]:
            for i in curr:
                x = huffman.encode_len(len(substr))
                y = huffman.encode_dist(start - i)
                if x and y:
                    refs[start].append((len(substr), x + y))
            curr.append(start)

    initial = State(0, BitString(0, 0))
    start, cost = merge(initial, huffman.raw, delim)

    dp = [{} for _ in range(len(data) + 2)]
    dp[0][start] = (cost, -1, initial, huffman.raw)

    for i in range(len(data) + 1):
        for state, (cost, _, _, _) in dp[i].items():
            code = huffman.encode_lit(data[i] if i < len(data) else 256)
            new_state, extra = merge(state, code, delim)

            if new_state not in dp[i + 1] or cost + extra < dp[i + 1][new_state][0]:
                dp[i + 1][new_state] = (cost + extra, i, state, code)

            for size, code in refs[i]:
                new_state, extra = merge(state, code, delim)
                if new_state not in dp[i + size] or cost + extra < dp[i + size][new_state][0]:
                    dp[i + size][new_state] = (cost + extra, i, state, code)

    codes, curr = [], min(dp[-1].values())
    while True:
        codes.append(curr[3])
        if curr[1] == -1:
            break
        curr = dp[curr[1]][curr[2]]

    combined = BitString(0, 0)
    for code in codes[::-1]:
        combined += code
    combined += BitString(0, -combined.size % 8)

    ret, _ = combined.to_bytes()
    return ret


def reencode(deflate, delim):
    if deflate[0] & 0b111 == 0b101:
        data = zlib.decompress(deflate, -10)
        return lz77(data, Huffman.parse(deflate), delim)
    return deflate
