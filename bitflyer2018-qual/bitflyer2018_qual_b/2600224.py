A_s,B_s,N_s = raw_input().split(" ")
X = raw_input()
A = int(A_s)
B =int(B_s)
N =int(N_s)


for char in X:
    if char == 'S':
        if A > 0:
            A = A - 1
    elif char == 'C':
        if B > 0:
            B = B - 1
    elif char == 'E':
        if A > 0:
            if A >= B:
                A = A - 1
            else:
                B = B - 1
        elif B > 0:
            B = B - 1

print A
print B
