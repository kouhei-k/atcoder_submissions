import collections
N=int(input())
c=input()+"1234"
C=collections.Counter(c).most_common()
print(C[0][1]-1,C[-1][1]-1)
