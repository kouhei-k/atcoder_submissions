N, Q = map(int, input().split())
S = input()
l = [0]*Q
r = [0]*Q

sum_arr = [0, 0]

for i in range(Q):
    l[i], r[i] = map(int, input().split())

for i in range(N-1):
    if S[i:i+2] == "AC":
        sum_arr.append(sum_arr[-1] + 1)
    else:
        sum_arr.append(sum_arr[-1])
for i in range(Q):
    print(sum_arr[r[i]] - sum_arr[l[i]])
