N = int(input())
d = dict()

d[0] = 'pon'
d[1] = 'pon'
d[2] = 'hon'
d[3] = 'bon'
d[4] = 'hon'
d[5] = 'hon'
d[6] = 'pon'
d[7] = 'hon'
d[8] = 'pon'
d[9] = 'hon'
print(d[N % 10])
