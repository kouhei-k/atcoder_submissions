A, B, C, K = map(int, input().split())

if K % 2 == 1:
    print(B-A)
else:
    print(-(B-A))
