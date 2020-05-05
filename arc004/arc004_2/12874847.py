N = int(input())
d = [int(input()) for i in range(N)]
print(sum(d))
if max(d)*2 < sum(d):
    print(0)
else:
    print(max(d)*2 - sum(d))
