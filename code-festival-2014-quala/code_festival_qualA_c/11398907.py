A, B = map(int, input().split())


def solve(N):
    ret = N // 4
    ret -= N // 100
    ret += N // 400
    return(ret)


print(solve(B) - solve(A-1))
