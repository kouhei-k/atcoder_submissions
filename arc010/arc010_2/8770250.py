import bisect
N = int(input())
md = [tuple(map(int, input().split("/"))) for i in range(N)]
md.sort(key=lambda x: x[0])
holidays = [[] for i in range(12)]
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = 1
flag = True  # Sunday
for i in range(1, 13):
    d -= days[i-1]
    while(d <= days[i]):
        holidays[i-1].append(d)
        if flag:
            d += 6
            flag = False
        else:
            d += 1
            flag = True

for m, d in md:
    while(1):
        id = bisect.bisect_left(holidays[m-1], d)
        if id == len(holidays[m-1]) or holidays[m-1][id] != d:
            bisect.insort_left(holidays[m-1], d)
            break
        else:
            d += 1
            if d > days[m]:
                m += 1
                d = 1
            if m > 12:
                break
ans=0
tmp=0
for i in range(12):
  for j in range(days[i+1]):
    if j+1 in holidays[i]:
      tmp+=1
    else:
      tmp=0
    ans=max(tmp,ans)

print(ans)
