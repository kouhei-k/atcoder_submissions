def func(y, m, d):
    if m == 1 or m == 2:
        m += 12
        y -= 1
    ret = 365*y + y // 4 - y // 100 + y//400 + (306*(m+1))//10 + d - 429
    return(ret)


y = int(input())
m = int(input())
d = int(input())
print(func(2014, 5, 17) - func(y, m, d))
