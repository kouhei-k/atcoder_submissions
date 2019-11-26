import math
H,W=map(int,input().split())
if H%3==0 or W%3==0:
  print(0)
  exit(0)
S=[0]*3
s=H*W/3
w0=math.ceil(s/H)
h0=math.ceil(s/W)

S[0]=w0*H
w1=W-W/3
w0=math.ceil(s/H)
h0=math.ceil(s/W)

S[0]=w0*H
w1=W-w0
if w1%2==0 or H%2==0:
  S[1]=(H*w1)//2
  S[2]=(H*w1)//2
else:
  s1=H*w1/2
  w10=math.ceil(s1/H)
  h10=math.ceil(s1/w1)
  S[2]=max((w1-w10)*H,(H-h10)*w1)
ans=abs(S[0]-S[2])

S[0]=W*h0
h1=H-h0
if h1%2==0 or W%2==0:
  S[1]=(W*h1)//2
  S[2]=(W*h1)//2
else:
  s1=h1*W/2
  w11=math.ceil(s1/h1)
  h11=math.ceil(s1/W)
  S[2]=max((W-w11)*h1,(h1-h11)*W)
ans=min(ans,abs(S[0]-S[2]))


S=[0]*3
s=H*W/3
w0=math.floor(s/H)
h0=math.floor(s/W)

S[0]=w0*H
w1=W-w0
if w1%2==0 or H%2==0:
  S[1]=(H*w1)//2
  S[2]=(H*w1)//2
else:
  s1=H*w1/2
  w10=math.floor(s1/H)
  h10=math.floor(s1/w1)
  S[2]=max((w1-w10)*H,(H-h10)*w1)
ans=min(ans,abs(S[0]-S[2]))

S[0]=W*h0
h1=H-h0
if h1%2==0 or W%2==0:
  S[1]=(W*h1)//2
  S[2]=(W*h1)//2
else:
  s1=h1*W/2
  w11=math.floor(s1/h1)
  h11=math.floor(s1/W)
  S[2]=max((W-w11)*h1,(h1-h11)*W)
ans=min(ans,abs(S[0]-S[2]))

print(ans)
