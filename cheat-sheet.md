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

## Other tricks

Getting the width as a variable in double list comprehension:

```python 
[[... for c in range(w)]for r in range(len(g))if(w:=len(g[0]))]
```
