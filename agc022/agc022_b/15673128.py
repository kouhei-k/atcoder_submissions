# 奇数は偶数個->偶数を除いたときに偶数なら公約数が２になる
import math
import collections
N = int(input())
# for N in range(20000, 2, -1):
ans = [2, 3, 25]
if N <= 1003:
    ans += [i for i in range(30, (N-3)*30+1, 30)]
    # print(*ans)
else:

    D = N - len(ans)
    for i in range(12, min(30000, (D//10)*20) + 1, 30):
        ans.append(i)
        ans.append(i+2)
        ans.append(i+4)
        ans.append(i+6)
        ans.append(i+8)
        ans.append(i+10)
        ans.append(i+12)
        ans.append(i+14)
        ans.append(i+16)
        ans.append(i+18)
    count = 0
    d = N - len(ans)
    for i in range(32, min(30000, (D//5)*10) + 1, 30):
        if i + 30 > min(30000, (D//5)*10) and (d - count*5) % 2 == 0:
            break

        count += 1
        ans.append(i)
        ans.append(i+2)
        ans.append(i+4)
        ans.append(i+6)
        ans.append(i+8)

    d = N - len(ans)
    # if d == 0:
    for i in range(33, min(30000, (d//4)*30 + 30)+1, 30):
        ans.append(i)
        ans.append(i+6)
        ans.append(i+18)
        ans.append(i+24)
    d = N - len(ans)
    for i in range(15, min(30000, (d//2)*60)+1, 60):
        ans.append(i)
        ans.append(i+30)

    d = N - len(ans)
    for i in range(325, min(30000, (d//2 - 1)*300 + 325)+1, 300):
        ans.append(i)
        ans.append(i+100)

print(*sorted(ans[:N]))
# S = sum(ans[:N])
# s = S
# t = 0
# while(S > 0):
#     t += S % 10
#     S //= 10
# k = collections.Counter(ans[:N]).most_common()

# if t % 3 != 0 or s % 10 != 0 or len(ans) < N or k[0][1] > 1:
#     print(ans[:N])
#     print(t, s, len(ans), N)
#     print(k[0])
#     break
# else:
#     print(N, t, s, len(ans))
