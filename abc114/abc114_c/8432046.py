import math
N = int(input())
if N < 357:
    print(0)
else:
    k = 1
    ans = 0
    while(10**k < N):
        k += 1
    
    nums=set()
    for i in range(1,4**k):
      num=0
      flag=[False,False,False,False]
      for j in range(k):
        tmp= (i // (4**j))%4
       
        if flag[3] and tmp<3:
          flag[tmp-1]=False
            
          break
        else:
          flag[tmp-1]=True
          
        if tmp==1:
          num+=3*(10**j)
        elif tmp==2:
          num+=5*(10**j)
        elif tmp==3:
          num+=7*(10**j)
        else:
          if j<3:
            break    
      
      #print(num,flag)
      for i in range(3):
        if flag[i]:
          if i == 2 and num<=N:
            nums.add(num)
        else:
          break
    forbidden=set()
    for x in nums:
      x=str(x)
      if "0" in x:
        forbidden.add(x)
    print(len(nums)-len(forbidden))
