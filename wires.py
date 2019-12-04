import sys

def make_wires():
    wire1 = {(0, 0): 0}
    wire2 = {(0, 0): 0}
    steps1 = 0
    steps2 = 0
    x, y = 0, 0
    closest = float('inf')

    def reset():
        nonlocal x, y
        x, y = 0, 0

    def move(direction, length, wire = 1):
        nonlocal x, y, steps1, steps2, closest
        dx, dy = 0, 0
        if direction == 'U':
            dy = -1
        elif direction == 'D':
            dy = 1
        elif direction == 'L':
            dx = -1
        elif direction == 'R':
            dx = 1
        for i in range(length):
            x += dx
            y += dy
            p = (x, y)
            if wire == 1:
                steps1 += 1
                if not p in wire1: wire1[p] = steps1
            else:
                steps2 += 1
                if not p in wire2: wire2[p] = steps2
            if p in wire1 and p in wire2 and wire1[p] + wire2[p] < closest:
                closest = wire1[p] + wire2[p]
        return closest

    return {'move': move, 'reset': reset}

def parse_line(s):
    return map((lambda ms: (ms[:1], int(ms[1:]))), s.strip().split(','))


wires = make_wires()
move = wires['move']
reset = wires['reset']

wire1 = sys.stdin.readline()
wire2 = sys.stdin.readline()

for d, l in parse_line(wire1): res = move(d, l)
reset()
for d, l in parse_line(wire2): res = move(d, l, 2)
print(res)
