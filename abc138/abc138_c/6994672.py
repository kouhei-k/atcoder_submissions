N = int(input())
v = list(map(int, input().split()))

def nabe(x,y):
    return (x + y) / 2

#for i in range(N - 1):
v = sorted(v)
for _ in range(N - 1):
    x = v.pop(0)
    y = v.pop(0)

    v.insert(0, nabe(x,y))

print(v[0])
