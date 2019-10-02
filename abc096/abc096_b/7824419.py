a=list(map(int,input().split()))
K=int(input())
maxa=a.pop(a.index(max(a)))
print((maxa*(2**K))+sum(a))
