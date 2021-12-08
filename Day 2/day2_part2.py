with open("input2.txt") as f:
    cmd = f.readlines()

cmd = [c.strip().split(" ") for c in cmd]

horizontal = 0
depth = 0
aim = 0

for c in cmd:
    if c[0] == "forward":
        horizontal += int(c[1])
        depth += aim * int(c[1])
    elif c[0] == "up":
        aim -= int(c[1])
    elif c[0] == "down":
        aim += int(c[1])

print("Horizontal", horizontal)
print("Depth", depth)
print("Multiplied", horizontal * depth)