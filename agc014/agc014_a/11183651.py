A, B, C = map(int, input().split())

if A % 2 or B % 2 or C % 2:
    print(0)
    exit(0)


def solve(n):
    i = 0
    while(n % 2 == 0):
        n = n // 2
        i += 1
    return(i)


a = solve(A+B)
b = solve(B+C)
c = solve(C+A)
if a == b and b == c:
    print(-1)
else:
    print(min(a, b, c))
