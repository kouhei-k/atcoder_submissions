K,T = map(int,input().split())
a = list(map(int,input().split()))

a = sorted(a,reverse = True)
ans = a.pop(0) - sum(a) - 1
if ans >= 0:
    print(ans)
else:
    print(0)
