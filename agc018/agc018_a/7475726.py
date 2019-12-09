import collections
N, K = map(int, input().split())
A = list(map(int, input().split()))
if K in A:
    print("POSSIBLE")
    exit(0)
else:
    diff = collections.defaultdict(int)
    A.sort()
    idx = N - 1
    if K > A[-1]:
        print("IMPOSSIBLE")
        exit(0)
    else:
        for i in range(N-1):
            if A[i] > K and idx == N - 1:
                idx = i
            if A[i+1] - A[i] != 0:
                diff[A[i+1] - A[i]] += 1

        diff_list = list(diff.keys())
        if 1 in diff_list:
            print("POSSIBLE")
            exit(0)
        else:
            diff_list.sort()
            for i in range(idx, N):
                for j in range(len(diff_list)):
                    if (K - A[i]) % diff_list[j] == 0:
                        print("POSSIBLE")
                        exit(0)
            print("IMPOSSIBLE")
            exit(0)
