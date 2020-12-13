L = int(input())
L -= 1
ans = 1
for i in range(11):
    ans *= L
    ans //= (i+1)
    L -= 1
print(ans)
