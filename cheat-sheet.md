## Most frequent color

Getting the most frequent color in a 2D grid (28 byte)

```python 
max(l:=sum(g,g),key=l.count)
```

If the 1D list is going to be reused (29 byte):
```python 
max(l:=sum(g,[]),key=l.count)
```

## Crop figure

Figure needs to be fully connected and surrounding must be black.

```python 
[r for*r,in zip(*filter(any,zip(*g)))if sum(r)]
```

## Other tricks

Getting the width as a variable in double list comprehension:

```python 
[[... for c in range(w)]for r in range(len(g))if(w:=len(g[0]))]
```
