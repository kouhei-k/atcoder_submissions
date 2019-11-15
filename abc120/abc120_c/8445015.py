S = input()
count = [0, 0]
for x in S:
    count[int(x)] += 1

print(min(count)*2)
