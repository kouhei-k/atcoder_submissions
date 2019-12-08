antennas = [0] * 5
for i in range(5):
    antennas[i] = int(input())

k = int(input())

for i in range(len(antennas)):
    for j in range(i + 1,len(antennas)):
        if antennas[j] - antennas[i] > k:
            print(":(")
            exit(0)

print('Yay!')
