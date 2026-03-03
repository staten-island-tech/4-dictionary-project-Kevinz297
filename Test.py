""" def occupied(x,y,t):
    for i in range(x):
        if (y[i] == "C" and t[i] == "C"):
            found += 1
    print(found)

occupied(5, "CCCCC", "CCCCC")
occupied(7, "CCCCCCC", "C.C.C.C") """

def language(T):
    t_count=0
    s_count=0
    for i in range(len(T)):
        if T[i] == "T":
            t_count += 1
    for i in range(len(S)):
        if T[i] == "S":
            s_count += 1
    if t_count > s_count:
        print("English")
    else:
        print("French")

    language(1, "TTTT")
