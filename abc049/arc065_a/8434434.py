S = input()
words = ["dream", "dreamer", "erase", "eraser"]

id = len(S)
while(id > 0):
    if S[:id].endswith("dream"):
        id -= 5
    elif S[:id].endswith("dreamer"):
        id -= 7
    elif S[:id].endswith("erase"):
        id -= 5
    elif S[:id].endswith("eraser"):
        id -= 6
    else:
        print("NO")
        exit(0)
print("YES")
