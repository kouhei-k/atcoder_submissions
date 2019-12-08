W,H,x,y = map(int,input().split())

ans= [(W*H / 2),0]
if x == W / 2 and y == H / 2:
    ans[1] = 1

print(" ".join(list(map(str,ans))))
