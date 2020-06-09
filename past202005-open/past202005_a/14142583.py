s = input()
t = input()

if s == t:
    print("same")
else:
    if s.upper() == t.upper():
        print("case-insensitive")
    else:
        print('different')
