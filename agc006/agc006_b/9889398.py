N, x = map(int, input().split())
if N == 2:
    if x != N:
        print("No")
        exit(0)
else:
    if abs(N - x) > N - 2:
        print("No")
        exit(0)
print("Yes")

if N == 2:
    for i in range(3):
        print(i+1)
else:
    left = []
    right = []
    if x < 2 * N - 2:
        ans = [x+2, x-1, x, x+1]
        s = [i for i in range(1, 2*N) if i < x - 1 or i > x+2]
        for i in range((2*N - 5) // 2):
            print(s.pop())
        for i in range(4):
            print(ans[i])
        for i in range(((2*N - 5) // 2) + 1):
            print(s.pop())

    else:
        ans = [x-2, x+1, x, x-1]
        s = [i for i in range(1, 2*N) if i < x - 2 or i > x+1]
        for i in range((2*N - 5) // 2):
            print(s.pop())
        for i in range(4):
            print(ans[i])
        for i in range(((2*N - 5) // 2) + 1):
            print(s.pop())
