from dama import show
from headlines import headline as hl


options = ["1. Show Index Filecontents", "2. Show Data Filecontents", "3. Exit"]


def dv():
    while True:
        print("\n".join(options))
        o = input("")
        if o == "1":
            print("")
            hl("Index", False, False, True, True)
            print("\n".join(show("i")))
        elif o == "2":
            print("")
            hl("Data", False, False, True, True)
            print("\n".join(show("d")))
        elif o == "3":
            break
