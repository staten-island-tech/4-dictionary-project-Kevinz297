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

""" 

def find_honi(sentence):
    HONI=["H", "O", "N", "I"]
    count = 0
    state = 0
    for honiblock in sentence:
        if HONI[state] == honiblock:
            state += 1
        if state >= 4:
            count += 1
            state = 0
    print(count)

find_honi("HHHHOOOONNNNIIII")


"""  
best_buy_items = [
    {"name": "DDR5 32 gigabyte Ram", "price": 999.99, "description": "High-performance RAM for gaming and content creation."},
    {"name": "Vbucks", "price": 499.99, "description": "In-game currency for Fortnite."},
    {"name": "Social Credit", "price": 199.99, "description": "A measure of your online reputation."},
    {"name": "Bitcoin", "price": 1.00, "description": "A decentralized digital currency."},
    {"name": "Robux", "price": 399.99, "description": "In-game currency for Roblox."}
]

for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])   