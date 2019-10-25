keyboard="WBWBWWBWBWBW"
S=input()
id=0
for i in range(12):
  if S.startswith(keyboard[i:]):
    id = i
    break
soundname=["Do","Do","Re","Re","Mi","Fa","Fa","So","So","La","La","Si"]
print(soundname[id])
