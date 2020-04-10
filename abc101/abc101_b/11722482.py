N = int(input())
s = N
tmp = 0

while(s > 0):
    tmp += s % 10
    s = s // 10

if N % tmp:
    print("No")
else:
    print("Yes")
