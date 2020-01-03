import math
N = int(input())
tmp = N
ans = []
# print("--------")
for i in range(len(bin(N))):
    # print(tmp % -2**(i+1), -2**(i+1))
    # print(tmp % 2**(i+1), 2**(i+1))
    k = tmp % -2**(i+1)
    # print("--------")
    if k == - 2**i:
        ans.append(1)
        tmp -= (-2)**i
    else:
        ans.append(0)
#print("".join(map(str, ans[::-1])))
tmp = 0
id = len(ans)
for i in range(len(ans)):
    if ans[i]:
        tmp += (-2)**i
    # print(tmp)
    if tmp == N:
        id = i+1
        break


ans = ans[:id]

print("".join(map(str, ans[::-1])))
