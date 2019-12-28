import sys
input = sys.stdin.readline
N, A, B = map(int, input().split())

if B < A:
    A, B = B, A

diff = B - A
if diff % 2 == 0:
    print(diff // 2)
else:
    ans = min(N-B, A-1) + (diff + 1) // 2
    print(ans)
