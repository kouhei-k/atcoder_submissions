A,B = map(int,input().split())

S = input()

if S[A] == "-":
    if S[:A].isdigit():
        if S[A+1:].isdigit():
            print("Yes")
            exit(0)

print("No")
