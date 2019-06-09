s = list(input())
K = int(input())

a_num = 97
z_num = 122

for i in range(len(s)):
    if K == 0:
        break
    else:
        if i == len(s) - 1:
          if ord(s[i])+ (K%26) <= z_num:
            s[i] = chr(ord(s[i]) + (K%26))
          else:
            s[i] = chr(ord(s[i]) + (K%26) - 26)

        elif ord(s[i]) == a_num:
            continue
        elif K >= z_num - ord(s[i]) + 1:
            K -= z_num - ord(s[i]) + 1
            s[i]="a"
        
print("".join(s))
