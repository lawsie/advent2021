with open("input.txt") as f:
    depths = f.readlines()

# This doesn't work - index out of range, and ran out of time to fix
depths = [1 if d < depths[i+1] else 0 for i, d in enumerate(depths)]


print(depths.count(1))