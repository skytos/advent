import sys

def fuel(mass):
	base = mass / 3 - 2
	if base <= 0: return 0
	return base + fuel(base)

total = 0
for line in sys.stdin.readlines():
	mass = int(line.strip())
	total += fuel(mass)
print total
