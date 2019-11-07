N=int(input())
a=list(map(int,input().split()))
diff = [max(0,80-a[i]) for i in range(N)]
print(sum(diff))
