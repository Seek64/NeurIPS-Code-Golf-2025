def p(g,n=7):
 l=len(g)*3+2;*h,=f"{*zip(*g[::-1]),}#"*3;i=-1
 for x,y in zip(h,h[3:l*25]):
  i+=1;s=[i]*(x>'0'<y!=x)
  for j in s:h[j-j%l+(i+i-j)%l+3]=y;s+={k for d in range(9)if h[k:=j+d//3*l-l+d%3*3-3]==x}-{*s}
 return-n*g or p(eval("".join(h)),n-1)