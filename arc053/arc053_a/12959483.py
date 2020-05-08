H,W = map(int, input().split())
ans = (H-1)*W
ans += (W-1)*H
print(ans)
