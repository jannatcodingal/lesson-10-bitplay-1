input("Build a bit mask - one 1 at exactly that position. Press Enter ")
for k in range(4):
    mask=1<<k
    print(" bit", k, " mask:", mask, " binary:", bin(mask)[2:])
    