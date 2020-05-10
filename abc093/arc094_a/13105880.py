ABC = list(map(int, input().split()))
ABC.sort()
A = ABC[2]
B = ABC[1]
C = ABC[0]
ans = A-B
C += ans
if (A - C) % 2 == 1:
    ans += (A+1-C)//2 + 1
else:
    ans += (A-C)//2
print(ans)
