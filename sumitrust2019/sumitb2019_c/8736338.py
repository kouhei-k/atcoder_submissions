X = int(input())

y = X % 105
z = X // 105

if y >= max(0, 100 - 5*z) or y == 0:
    print(1)
else:
    print(0)
