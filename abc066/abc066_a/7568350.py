abc=list(map(int,input().split()))
abc.sort()
print(sum(abc)-abc[-1])
