d = dict()
d["b"]=1
d["c"]=1
d["d"]=2
d["w"]=2
d["t"]=3
d["j"]=3
d["f"]=4
d["q"]=4
d["l"]=5
d["v"]=5
d["s"]=6
d["x"]=6
d["p"]=7
d["m"]=7
d["h"]=8
d["k"]=8
d["n"]=9
d["g"]=9
d["z"]=0
d["r"]=0
def reform(word):
  s={"a","i","u","e","o","y",",","."}
  ret = []
  for x in word:
    x=x.lower()
    if x in s:
      continue
    else:
      ret.append(d[x])
  ret="".join(map(str,ret))
  return(ret)
N=int(input())
S=list(map(reform,input().split()))
ans=[]
for x in S:
  if len(x)>0:
    ans.append(x)
print(" ".join(ans))
