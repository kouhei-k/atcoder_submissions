import math
N = int(input())
k = math.ceil(N / 9)

ans = [str((N+(k-1)) % 10)] * k
print("".join(ans))
