""" def occupied(x,y,t):
    for i in range(x):
        if (y[i] == "C" and t[i] == "C"):
            found += 1
    print(found)

occupied(5, "CCCCC", "CCCCC")
occupied(7, "CCCCCCC", "C.C.C.C") """
""" 
""" 
t = "t"
s = "s"
def language(t):
    t_count=0
    s_count=0
    for i in range(len(t)):
        if t[i].lower() == "t":
            t_count += 1
            print("English")
        elif s[i].lower() == "s":
            s_count += 1
            print("French")

language("SSSS")
