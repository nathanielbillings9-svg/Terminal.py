def dve():
    import dama

    while True:
        instr = input("dve:")
        if instr == "exit":
            break
        elif instr == "help":
            print(
                "'exit', 'r <name>', 'w <name> <data>', 'c <name> <data>', 'd <name>', 'sd', 'si', 'sf'"
            )
        elif instr.startswith("r "):
            print(dama.read(instr[2:]))
        elif instr.startswith("w "):
            instrdata = instr.split(maxsplit=2)
            dama.write(instrdata[1], instrdata[2])
        elif instr.startswith("c "):
            instrdata = instr.split(maxsplit=2)
            dama.change(instrdata[1], instrdata[2])
        elif instr.startswith("d "):
            dama.delete(instr[2:])
        elif instr == "sd":
            print("Data in " + dama.file("d") + ": " + str(dama.show("d")))
        elif instr == "si":
            print("Index in " + dama.file("i") + ": " + str(dama.show("i")))
        elif instr == "sf":
            print("Index File: " + dama.file("i"))
            print("Data File: " + dama.file("d"))
