## Most frequent color

Getting the most frequent color in a 2D grid (28 byte)

```python 
max(l:=sum(g,g),key=l.count)
```

If the 1D list is going to be reused (29 byte):
```python 
max(l:=sum(g,[]),key=l.count)
```

## Filter zeros from 1D list

```python 
[*filter(int,l)]
```

## Upscale 

Upscale by 2. Still not optimal, see Problem 307.

```python 
[[*sum(zip(r,r),())]for r in sum(zip(g,g),())]
```

## Iterating over column and row 

```python 
[[v for*c,v in zip(*g,r)]for r in g]
```

## Crop figure

Figure needs to be fully connected and surrounding must be black.

```python 
[r for*r,in zip(*filter(any,zip(*g)))if sum(r)]
```

## Short any()

If the first row is all black (which is often guaranteed by the generator), -2 bytes using:

```python
[...for r in g if any(g)]
[...for r in g if[r]>g]
```

## Depth 2 Recursion

```python
p=lambda g,h=0:[...for r in zip(*h or p(g,g))]
```

## 1-D Rotate right

```python
[g.pop()]+g
```

# Regex

Many draw task can be used with the following "rotate-and-replace" strategy.
The upper one is 1 byte shorter if few rotations are needed.

```python 
import re;p=lambda g:[g:=eval(re.sub("","",f"{[*zip(*g[::-1])]}"))for _ in g][3]
import re;p=lambda g,k=99:-k*g or p(eval(re.sub("","",f"{[*zip(*g[::-1])]}")),k-1)
```

If multiple different regex are required, one can do:

```python 
import re;p=lambda g:[g:=eval(re.sub(*s,f"{[*zip(*g[::-1])]}"))for s in[("","")]*M+[("","")]*N][-1]
```

If you need to fill the inside of a shape, the regex expression often looks something like this.
In this example, we replace all 0 that have a right and bottom 1 with a 1.
The "len(g)" can often be hardcoded if the field is a fixed-size square.

```python 
re.sub("0(?=, 1.{%d}1)"%(3*len(g)-2),"1",f"{[*zip(*g[::-1])]}")
```
