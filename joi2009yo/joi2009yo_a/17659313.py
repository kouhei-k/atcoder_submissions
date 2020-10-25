for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    H = h2 - h1
    M = m2 - m1
    S = s2 - s1
    if S < 0:
        S = 60 + S
        M -= 1
    if M < 0:
        H -= 1
        M = 60 + M

    print(H, M, S)
