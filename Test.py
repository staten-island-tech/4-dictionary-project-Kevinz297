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
""" Game_Currency = [
    {"name": "DDR5 32 gigabyte Ram", "price": 999.99, "description": "High-performance RAM for gaming and content creation."},
    {"name": "Vbucks", "price": 499.99, "description": "In-game currency for Fortnite."},
    {"name": "Social Credit", "price": 199.99, "description": "A measure of your online reputation."},
    {"name": "Bitcoin", "price": 1.00, "description": "A decentralized digital currency."},
    {"name": "Robux", "price": 399.99, "description": "In-game currency for Roblox."}
]
for index, item in enumerate(Game_Currency):
    print(index, ":", item["name"]) 
Store = Game_Currency
Cart = []
total = 0
Shopping = "yes"
while Shopping == "yes":
    for i in range(len(Store)):
        print(i, "-", Store[i]["name"], "$", Store[i]["price"])
    choice = int(input("Pick an item number: "))
    Cart.append(Store[choice]["name"])
    total = total + Store[choice]["price"]
    Shopping = input(" Do you want to continue shopping? (yes/no): ")
print("Items bought:")
for item in Cart:
    print(item)
print("Total:", total)
 """
""" def slot_m(q, m1, m2, m3):
    m1_played = m1
    m2_played = m2
    m3_played = m3
    while q > 0:
        q -= 1
        m1_played += 1
        if q==0:
            break
        if m1_played % 35 == 0:
            q += 30

        q -= 1
        m2_played += 1
        if q==0:
            break
        if m2_played % 100 == 0:
            q += 60

        q -= 1
        m3_played += 1
        if q==0:
            break
        if m3_played % 10 == 0:
            q += 9
    x = m1_played-m1+m2_played-m2+m3_played-m3
    print(f"Martha played {x} times before going broke.")
slot_m(77,4,9,3)  """ 

def plantations (N, H):
    current_increase_streak=1
    current_decrease_streak=2
    longest_increase_streak=1
    longest_decrease_streak=1
    for track in range(int(N)-1):
        if H[track] < H[track+1]:
            current_increase_streak += 1
            if current_decrease_streak > longest_decrease_streak:
                longest_decrease_streak = current_decrease_streak
                current_decrease_streak = 1

        elif H[track] > H[track+1]:
            current_decrease_streak += 1
            if current_increase_streak > longest_increase_streak:
                longest_increase_streak = current_increase_streak
                current_increase_streak = 1

    print(longest_increase_streak)
    print(longest_decrease_streak)

plantations(4, [1, 3, 4, 2])