N = int(input())
n = sum(list(map(int, str(N))))

if N % n == 0:
    print("Yes")
else:
    print("No")
