N = int(input())
s = [input() for i in range(N)]

s.sort(key=lambda x: x[::-1])

for x in s:
    print(x)
