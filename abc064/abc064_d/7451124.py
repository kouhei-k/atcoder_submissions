N=int(input())
S=input()
S3=[]
for i in range(len(S)):
  S3.append(S[i])
  if S3.count("(") < S3.count(")") :
    S3 =["("] + S3
  if i == len(S) - 1:
    for j in range(S3.count("(") - S3.count(")")):
      S3.append(")")
      
print("".join(S3))
