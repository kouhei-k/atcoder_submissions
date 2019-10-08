A,B,K = map(int, input().split())
ans = []
if A + K - 1< B - K + 1:
    ans = [A + i for i in range(K)] + [B - i for i in reversed(range(K))]

else:
    if A + K - 1 < B and A <= B - K + 1:
        ans = [A + i for i in range(K)] + [B - i for i in reversed(range(B - (A + K - 1)))]
    else:
        ans = [i for i in range(A,B+1)]

for i in range(len(ans)):
    print(ans[i])
