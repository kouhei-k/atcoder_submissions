def main():
  N, x = map(int, input().split())
  a = list(map(int, input().split()))
  c = [a[i] for i in range(N)]
  ans = sum(a)
  for i in range(N):
    tmp = i*x
    for j in range(N):
      c[j]=min(c[j],a[j-i])
      tmp += c[j]
    ans=min(ans,tmp)
  print(ans)
main()
