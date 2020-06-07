import sys


def ask(a, b):
    print('?', a, b)
    sys.stdout.flush()
    ret = int(input())
    return(ret)


def main():
    N = int(input())
    ans = 0
    dis = 0
    node = 0
    for i in range(2, N+1):
        ret = ask(1, i)
        if dis < ret:
            dis = ret
            node = i
    for i in range(1, N+1):
        if i == node:
            continue
        else:
            ans = max(ans, ask(node, i))
    print('!', ans)


main()
