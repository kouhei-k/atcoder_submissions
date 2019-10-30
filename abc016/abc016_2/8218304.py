A, B, C = map(int, input().split())
if A+B != A-B:
    if C == A+B:
        print("+")
    elif C == A-B:
        print("-")
    else:
        print("!")
else:
    if A+B == C:
        print("?")
    else:
        print("!")
