def main():
    from collections import Counter
    import sys
    input = sys.stdin.buffer.readline

    _ = int(input())
    A = [int(i) for i in input().split()]

    ans = 0
    c = Counter(A)
    B = sorted(c.keys(), reverse=True)

    for b in B:
        if c[b] == 0:
            continue
        a = (2 ** b.bit_length()) - b
        if a == b:
            cur = c[b]//2
        else:
            if a in c:
                cur = min(c[a], c[b])
            else:
                cur = 0
        ans += cur
        # c[b] -= cur
        c[a] -= cur

    print(ans)


if __name__ == '__main__':
    main()
