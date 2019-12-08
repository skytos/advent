import sys

with open(sys.argv[1]) as fin:
    script = fin.read()

state = list(map(int, script.strip().split(',')))

def run(state):
    pc = 0
    def get(modes, param):
        mode = 0
        if param - 1 < len(modes):
            mode = modes[param - 1]
        if mode == 1: return state[pc+param]
        else: return state[state[pc+param]]
    while True:
        op = state[pc]
        modes = []
        mode = op // 100
        while mode != 0:
            modes.append(mode % 10)
            mode //= 10

        op = op % 100
        if op == 1:
            state[state[pc+3]] = get(modes, 1) + get(modes, 2)
            pc += 4
        elif op == 2:
            state[state[pc+3]] = get(modes, 1) * get(modes, 2)
            pc += 4
        elif op == 3:
            state[state[pc+1]] = int(sys.stdin.readline().strip())
            pc += 2
        elif op == 4:
            print(get(modes, 1))
            pc += 2
        elif op == 99:
            break
    return state[0]

run(state)

def patch(state, noun, verb):
    new_state = state[:]
    new_state[1] = noun
    new_state[2] = verb
    return new_state

def day2():
    print(run(patch(state, 12, 2)))
    for noun in range(0, 100):
        for verb in range(0, 100):
            if run(patch(state, noun, verb)) == 19690720:
                print(noun*100 + verb)
