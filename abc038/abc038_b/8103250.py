hw1=list(map(int,input().split()))
hw2=list(map(int,input().split()))
for x in hw2:
  if x in hw1:
    print("YES")
    exit(0)
print("NO")
