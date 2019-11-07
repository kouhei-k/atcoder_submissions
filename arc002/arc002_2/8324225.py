y,m,d=map(int,input().split("/"))
date=[-1,31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(y,3000):
  for j in range(1,13):
    if i==y:
      if j < m:
        continue
    for k in range(1,date[j]+1):
      if i==y and j ==m:
        if k < d:
          continue
      if j == 2 and (i%4 != 0 or (i%100==0 and i%400!=0)) and k ==29:
        continue
      if i % (j*k) ==0:
        print(str(i)+"/"+str(j).zfill(2)+"/"+str(k).zfill(2))
        exit(0)
print("3000/01/01")
