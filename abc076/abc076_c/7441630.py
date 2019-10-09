S_ = input()
T = input()


def check(S1, S2):
    for i in range(len(S1)):
        if S1[i] == S2[i] or S1[i] == "?":
            continue
        else:
            return(False)

    return(True)


ans_list = []
for i in reversed(range(len(S_) - len(T) + 1)):
    result = check(S_[i:i+len(T)], T)
    if result:
        ans = list(S_)
        for j in range(len(T)):
            ans[i+j] = T[j]
        for j in range(len(ans)):
            if ans[j] == "?":
                ans[j] = "a"
        ans_list.append("".join(ans))

if len(ans_list) == 0:
    print("UNRESTORABLE")
else:
    print(min(ans_list))
