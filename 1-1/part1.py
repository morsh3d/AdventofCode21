with open('input_test.txt', 'r') as f:
    depths = f.read()
    count = 0
    for i in range(len(depths) - 1):
        if int(depths[i]) < int(depths[i + 1]):    # Compare current with “the next”
            count += 1

    print(count)


