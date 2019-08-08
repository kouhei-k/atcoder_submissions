N,K = map(int,input().split())
A=list(map(int,input().split()))
sumA = sum(A)

divisors = []
for i in range(1, int(sumA**0.5)+1):
    if sumA % i ==0:
        divisors.append(i)
        if  i != sumA // i:
            divisors.append(sumA//i)

ans = 0

for i in divisors:
    listA = [0]*N
    for j in range(N):
        listA[j] = A[j] % i
    listA.sort()
    sumlist = sum(listA)


    if sum(listA[:-sumlist // i]) <= K:
        ans = max(ans,i)
            
print(ans)
