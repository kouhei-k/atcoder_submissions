a,b,c,x,y=map(int,input().split())
ans=a*x+b*y
ans=min(ans,c*x*2 +max(0,y-x)*b,c*y*2+max(0,x-y)*a)
print(ans)
