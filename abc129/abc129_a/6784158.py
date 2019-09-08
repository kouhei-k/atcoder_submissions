P,Q,R=map(int,input().split())
abc=P+Q
bca=Q+R
cab=P+R
ans=[abc,bca,cab]
print(min(ans))
