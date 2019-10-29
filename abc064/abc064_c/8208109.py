N = int(input())
a = list(map(int, input().split()))
r_table = [1, 400, 800, 1200, 1600, 2000, 2400, 2800, 3200]
rate = [0]*8
god = 0
for x in a:
    for id, y in enumerate(r_table):
        if x >= y:
            if id == 8:
                god += 1
                break
        else:
            rate[id-1] = 1
            break
print(max(sum(rate), 1), sum(rate) + god)
