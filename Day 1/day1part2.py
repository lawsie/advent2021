with open("input.txt") as f:
    depths = f.readlines()
depths = [int(depth) for depth in depths]



larger = 0
prev_sum = depths[0] + depths[1] + depths[2]
for i, d in enumerate(depths):

    if i < len(depths)-2:
        window = d + depths[i+1] + depths[i+2]
        print("Looking at ", d, depths[i+1], depths[i+2], "which equals", window )

        
        if window > prev_sum:
            larger += 1
            print("bigger")
        prev_sum = window

print(larger)