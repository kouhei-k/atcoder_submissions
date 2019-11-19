S = input()
goal = "keyence"
if S.startswith(goal) or S.endswith(goal):
    print("YES")
else:
    for i in range(len(S)-1):
        if S.startswith(goal[:len(S)-i]) and S.endswith(goal[len(S)-i:]):
            print("YES")
            exit(0)
    print("NO")
