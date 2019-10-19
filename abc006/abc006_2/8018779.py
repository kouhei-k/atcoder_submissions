n = int(input())
ans = 0
if n == 1 or n == 2:
    print(0)
elif n == 3:
    print(1)
else:

    prev = [0, 0, 1]
    for i in range(n-3):
        prev = [prev[1], prev[2], sum(prev) % 10007]

    print(prev[2])
