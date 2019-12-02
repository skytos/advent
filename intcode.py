import sys

state = map(int, sys.stdin.readline().strip().split(','))

def run(state):
    pc = 0
    while True:
        op = state[pc]
        if op == 1:
            state[state[pc+3]] = state[state[pc+1]] + state[state[pc+2]] 
            pc += 4
        elif op == 2:
            state[state[pc+3]] = state[state[pc+1]] * state[state[pc+2]] 
            pc += 4
        elif op == 99:
            break
    return state[0]

def patch(state, noun, verb):
    new_state = state[:]
    new_state[1] = noun
    new_state[2] = verb
    return new_state

print(run(patch(state, 12, 2)))
for noun in range(0, 100):
    for verb in range(0, 100):
        if run(patch(state, noun, verb)) == 19690720:
            print(noun*100 + verb)
