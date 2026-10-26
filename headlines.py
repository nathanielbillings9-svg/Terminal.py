import pyfiglet

def headline(text, big, upper, lower, space):
    if upper:
        print("-" * len(str(text)))
    if big:
        print(pyfiglet.figlet_format(str(text)))
    else:
        print(str(text))
    if lower:
        print("-" * len(str(text)))
    if space:
        print("")