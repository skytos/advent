import sys

fuel = 0
for line in sys.stdin.readlines():
	mass = int(line.strip())
	fuel += mass / 3 - 2
print fuel
