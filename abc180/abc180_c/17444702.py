N = int(input())
s = set()
for i in range(1, int(N**(0.5))+1):
    if N % i == 0:
        s.add(i)
        s.add(N//i)
s = list(s)
s.sort()

print(*s, sep='
')
