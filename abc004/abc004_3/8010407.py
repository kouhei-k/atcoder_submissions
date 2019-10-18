N = int(input())
arr = [1,2,3,4,5,6]
k = (N // 5)%6
arr= arr[k:]+arr[:k]
for i in range(N%5):
  k= i%5
  arr[k],arr[k+1]=arr[k+1],arr[k]
  
print("".join(map(str,arr)))
