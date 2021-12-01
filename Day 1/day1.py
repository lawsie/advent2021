with open("input.txt") as f:
    depths = f.readlines()
depths = [int(depth) for depth in depths]



larger = 0
prev = depths[0]
for depth in depths:
    if depth > prev:
        larger += 1
    prev = depth
print(larger)