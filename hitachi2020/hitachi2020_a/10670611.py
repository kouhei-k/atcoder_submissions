s = input()
if len(s) % 2 != 0 or len(s) == 0:
    print("No")
else:
    for i in range(0, len(s), 2):
        if s[i] + s[i+1] == "hi":
            continue
        else:
            print("No")
            exit(0)
    print("Yes")
