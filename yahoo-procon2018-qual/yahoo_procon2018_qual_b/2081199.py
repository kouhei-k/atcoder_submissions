def ceil(X, K):
    range = pow(10,K)
    return ((int)(X / range) + 1 ) * range

input_line = raw_input().rstrip().split(' ')
X = int(input_line[0])
K = int(input_line[1])

ans = ceil(X,K)
print ans
