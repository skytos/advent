def check(p):
    last = 10
    same = 1
    pair = False
    while p != 0:
        x = p % 10
        if x == last:
            same += 1
        elif x > last:
            return False
        else:
            if same == 2: pair = True
            same = 1
        last = x
        p //= 10
    if same == 2: pair = True
    return pair

#ts = [11, 1337, 133444, 11122233]
#fs = [3, 222, 2223333, 32, 12231, 40112]
#print(list(map(check, ts)))
#print(list(map(check, fs)))
count = 0
for i in range(231832, 767346+1):
    if check(i): count += 1
print(count)
