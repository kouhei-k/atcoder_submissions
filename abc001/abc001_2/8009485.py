m = int(input())

if m < 100:
    print("00")
elif m <= 5000:
    if m < 1000:
        print("0" + str(m // 100))
    else:
        print(m // 100)
elif m >= 6000 and m <= 30000:
    print((m // 1000) + 50)
elif m >= 35000 and m <= 70000:
    print((((m // 1000) - 30) // 5) + 80)
elif m >= 70:
    print("89")
