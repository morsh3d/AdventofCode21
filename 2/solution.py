INPUT_FILE = "input_test.txt"
with open(INPUT_FILE, "r") as f:

    fwd1 = 0
    depth1 = 0

    fwd2 = 0
    depth2 = 0
    aim = 0

    for line in f:
        cmd,amt = line.split()
        amt = int(amt)
        if cmd == 'forward':
            fwd1 += amt
            fwd2 += amt
            depth2 += amt*aim
        elif cmd == 'up':
            depth1 -= amt
            aim -= amt
        else:
            assert cmd == 'down'
            depth1 += amt
            aim += amt
    # Answer to Part 1:
    print(fwd1*depth1)
    
    # Answer to Part 2:
    print(fwd2*depth2)