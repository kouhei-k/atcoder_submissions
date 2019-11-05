import collections
N = int(input())
table = collections.defaultdict(int)

for i in range(N):
    now = input()
    table[now] += 1
    if i == 0:
        prev = now[-1]
    else:
        if table[now] >= 2 or now[0] != prev:
            if i % 2 == 0:
                print("LOSE")
            else:
                print("WIN")
            exit(0)
        prev = now[-1]
print("DRAW")
