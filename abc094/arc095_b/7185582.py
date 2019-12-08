n = int(input())
a = list(map(int, input().split()))


ans=a.pop(a.index(max(a)))

for i in range(n - 1):
    if a[i] > ans / 2:
        a[i] = [ans - a[i],a[i]]
    else:
        a[i] = [a[i],a[i]]
a = sorted(a,reverse = True)

print(str(ans) + " " + str(a[0][1]))
