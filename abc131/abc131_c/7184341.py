import fractions
A,B,C,D = map(int,input().split())

lcm = int(C*D / fractions.gcd(C,D))
ans_b = B - (B // C) - (B // D) + (B // lcm)
ans_a = A - 1 - ((A - 1)// C) - ((A - 1)// D) + ((A - 1) // lcm)

print(int(ans_b - ans_a))
