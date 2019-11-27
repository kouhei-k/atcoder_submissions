A, B, C = map(int, input().split())

if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    print(0)
else:
    ans = [B*C, A*C, A*B]
    print(min(ans))
