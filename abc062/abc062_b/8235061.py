H,W=map(int,input().split())
ans=[[] for i in range(H+2)]
ans[0]=["#"]*(W+2)
ans[H+1]=["#"]*(W+2)
for i in range(1,H+1):
  ans[i]="#"+input()+"#"
for i in range(H+2):
  print("".join(ans[i]))
