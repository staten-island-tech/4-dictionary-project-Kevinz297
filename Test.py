""" def occupied(x,y,t):
    for i in range(x):
        if (y[i] == "C" and t[i] == "C"):
            found += 1
    print(found)

occupied(5, "CCCCC", "CCCCC")
occupied(7, "CCCCCCC", "C.C.C.C") """
""" 
""" 
""" t = "t"
s = "s"
def language(t):
    t_count=0
    s_count=0
    for i in range(len(t)):
        if t[i].lower() == "t":
            t_count += 1
        elif t[i].lower() == "s":
            s_count += 1

    if t_count > s_count:
        print("English")
    else:
        print("French")

language("TTTT")
 """
h = "h" 
o = "o"
n = "n"
i = "i"
honi_amount = 0
def find_honi(sentence):
    words = sentence.split()
    for honi in words:
        search_term = h + o + n + i
        if search_term in honi.lower():
            print("Found {0}: {1}".format(honi + 1, honi))
            return
        print("0")
find_honi("honi")
