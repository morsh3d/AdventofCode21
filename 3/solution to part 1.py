ans = 0
V0 = {}
V1 = {}
INPUT_FILE = "input_test.txt"
with open(INPUT_FILE, "r") as f:
    for line in f:
        line = line.strip()
        for i,c in enumerate(line):
            if i not in V0:
                V0[i] = 0
            if i not in V1:
                V1[i] = 0
            if  c=='1':
                V1[i] += 1
            else:
                V0[i] += 1
    gamma = ''
    epsilon = ''
    for i in V0:
        if V0[i] > V1[i]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
print(int(gamma,2)*int(epsilon,2))
