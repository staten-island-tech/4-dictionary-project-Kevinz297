def occupied(x,y,t):
    for i in range(x):
        if (y[i] == "C" and t[i] == "C"):
            found += 1
    print(found)

occupied(5, "CCCCC", "CCCCC")
occupied(7, "CCCCCCC", "C.C.C.C")
