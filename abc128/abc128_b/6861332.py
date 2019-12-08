N = int(input())
guide = [[0]] * N

for i in range(N):
  guide[i]= [i + 1]
  guide[i] += input().split()
  guide[i][2] = int(guide[i][2])

guide.sort(key = lambda x:x[2], reverse = True)
guide.sort(key = lambda x:x[1])

for i in range(N):
    print(guide[i][0])


  
