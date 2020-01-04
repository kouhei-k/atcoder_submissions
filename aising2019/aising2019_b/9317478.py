import bisect
N = int(input())
A,B = map(int, input().split())
P = list(map(int, input().split()))
P.sort()
ans = N
id = bisect.bisect_right(P,A)
ans = min(ans,id)
prev = id
id = bisect.bisect_right(P,B)
ans = min(ans,id - prev)
ans = min(ans,N - id)
print(ans)
