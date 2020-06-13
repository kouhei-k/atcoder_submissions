A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
D = abs(B - A)
if (V - W)*T >= D:
    print("YES")
else:
    print("NO")
