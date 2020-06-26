S="DiscoPresentsDiscoveryChannelProgrammingContest2016"
W=int(input())
prev=0
while(prev<len(S)):
  print(S[prev:min(prev+W,len(S))])
  prev+=W
