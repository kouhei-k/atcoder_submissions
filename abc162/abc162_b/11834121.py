N = int(input())

s = (1+N)*N // 2
s1 = 0
s2 = 0
s3 = 0
if N >= 3:
    s1 = ((3 + (N//3)*3) * (N//3)) // 2
if N >= 5:
    s2 = ((5 + (N//5)*5) * (N//5)) // 2
if N >= 15:
    s3 = ((15 + (N//15)*15) * (N//15)) // 2
print(s + s3 - s1 - s2)
