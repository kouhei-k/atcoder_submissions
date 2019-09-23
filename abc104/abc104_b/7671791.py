S = input()
if S[0] == "A":
    flag = False
    for i, x in enumerate(S[2:-1]):
        if x == "C":
            if flag:
                flag = False
                break
            else:
                flag = True
                index = i+2
    if flag:

        if (len(S[1:index]) == 0 or S[1:index].islower()) and (len(S[index+1:]) == 0 or S[index+1:].islower()):
            print("AC")
        else:
            print("WA")
    else:
        print("WA")
else:
    print("WA")
