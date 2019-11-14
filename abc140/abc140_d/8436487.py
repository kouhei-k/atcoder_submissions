N, K = map(int, input().split())
S = list(input())
count = 0
for i in range(N):
    if S[i] == "L":
        if i == 0:
            count += 1
        else:
            if S[i-1] == "R":
                count += 1
    else:
        if i == N-1:
            count += 1
        else:
            if S[i+1] == "L":
                count += 1

if (count-1) / 2 <= K:
    print(N-1)

else:
    print(N - (count - 2*K))
