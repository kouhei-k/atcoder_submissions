S = input()
T = input()

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    else:
        if S[i] == "@":
            if T[i] == "@":
                continue
            else:
                if T[i] in "atcoder":
                    continue
                else:
                    print("You will lose")
                    exit(0)
        elif T[i] == "@":
            if S[i] in "atcoder":
                continue
            else:
                print("You will lose")
                exit(0)
        else:
            print("You will lose")
            exit(0)

print("You can win")
