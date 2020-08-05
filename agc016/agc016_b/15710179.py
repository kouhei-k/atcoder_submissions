N = int(input())
a = list(map(int, input().split()))
M = max(a)
m = min(a)
if M > m + 1:
    print("No")
else:
    if M == m:
        if M == N-1:
            print("Yes")
        elif M*2 <= N:
            print("Yes")
        else:
            print("No")

    else:
        # ai == m　ならば、ai以外にその色はない
        c = a.count(m)
        if (M - c) * 2 <= N-c and c < M:  # (M-c) -> 一人だけではない色の種類一人だけではないはずなので*2 したものよりも残りの人数が多いはず
            print("Yes")
        else:
            print("No")
