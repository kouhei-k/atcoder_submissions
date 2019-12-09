N=int(input())
A=list(map(int,input().split()))
A.sort()
sum_arr=[0]*(N+1)
for i in range(N):
  sum_arr[i+1]=sum_arr[i]+A[i]
count=0
for i in range(1,N):
  if sum_arr[i]*2 >= A[i]:
    count+=1
  else:
    count=0
print(count+1)
