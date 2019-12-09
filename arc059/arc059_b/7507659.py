s = input()
l = len(s)
for i in range(l-1):
    if s[i] == s[i+1]:
        print(str(i+1) + " " + str(i+2))
        exit(0)

    elif i != l - 2:
        if s[i] == s[i+2]:
            print(str(i+1) + " " + str(i+3))
            exit(0)


print("-1 -1")
