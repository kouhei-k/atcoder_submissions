import collections
N=int(input())
siritori=collections.defaultdict(int)
prev=" "
for i in range(N):
  word = input()
  if word in siritori:
    print("No")
    exit(0)
  elif prev[-1]!=word[0] and i != 0:
    print("No")
    exit(0)
  siritori[word]+=1
  prev=word
print("Yes")
