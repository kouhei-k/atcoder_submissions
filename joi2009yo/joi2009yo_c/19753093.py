def main():
  import sys
  input = sys.stdin.buffer.readline
  N = int(input())
  A = [int(input()) for i in range(N)]

  S = []
  c = A[0]
  n = 1
  for x in A[1:]:
    if x == c:
      n += 1
    else:
      S.append([c,n])
      c = x
      n = 1
  S.append((c,n))

  ans = N - 1
  L = len(S)
  for i in range(L):
    x, c = S[i]
    if c == 1:
      tmp = N - 1
      if i == 0:
        if S[1][1] == 3:
          tmp -= 3
      elif i == L-1:
        if S[L-2][1] == 3:
          tmp -= 3
      elif S[i+1][0] == S[i-1][0] and S[i+1][1] + S[i-1][1] > 2:
        l = i-1
        r = i+1
        while(l >= 0 and r < L and S[l][0] == S[r][0] and S[l][1] + S[r][1] > 3):
          tmp -= S[l][1] + S[r][1]
          l -= 1
          r += 1
      if tmp < ans:
        ans = tmp

    else:
      if i > 0 and S[i-1][1] == 3:
        S[i][1] -= 1
        tmp = N - 4
        l = i-2
        r = i
        while(l >= 0 and r < L and S[l][0] == S[r][0] and S[l][1] + S[r][1] > 3):
          tmp -= S[l][1] + S[r][1]
          l -= 1
          r += 1
        if tmp < ans:
          ans = tmp
        S[i][1] += 1
      if i < L - 1 and S[i+1][1] == 3:
        S[i][1] -= 1
        tmp = N - 4
        l = i
        r = i+2
        while(l >= 0 and r < L and S[l][0] == S[r][0] and S[l][1] + S[r][1] > 3):
          tmp -= S[l][1] + S[r][1]
          l -= 1
          r += 1
        if tmp < ans:
          ans = tmp
        S[i][1] += 1
  print(ans)
         
main()
