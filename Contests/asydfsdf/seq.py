for i in range(int(1e8), int(1e8)+101):
    print(i, sum([int(x) for x in bin(i)[2:]]))