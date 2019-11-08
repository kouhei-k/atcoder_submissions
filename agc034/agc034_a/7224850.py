import copy
N,A,B,C,D = map(int,input().split())
S = input()

for i in range(A,max(C,D)-1):
    if S[i:i+2] == "##":
        print("No")
        exit(0)

if C > D:
    flag = False
    for i in range(B-1,D):
        if S[i-1:i + 2] == "...":
            flag = True
            break

    if flag == False:
        print("No")
        exit(0)

print("Yes")
