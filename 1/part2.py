INPUT_FILE = "input_test.txt"
with open(INPUT_FILE, "r") as f:
    depths = [int(line) for line in f]

count = 0
for i in range(len(depths) - 3):
    # We sum the windows we build with slices:
    left, right = sum(depths[i:i + 3]), sum(depths[i + 1:i + 4])
    if left < right:
        count += 1

print(count)