

def main():
    import sys

    input = sys.stdin.readline
    N = int(input())
    prev = 0
    x = 0
    y = 0

    for i in range(N):
        a, b, c = map(int, input().split())
        dis = abs(b - x) + abs(c - y)
        diff = a - prev
        if diff >= dis and diff % 2 == dis % 2:
            prev = a
            x = b
            y = c
        else:
            print("No")
            exit(0)
    print("Yes")


main()
