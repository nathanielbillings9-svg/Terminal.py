def vdc():
    print(
        "Vin = Input Voltage, Vout = Output Voltage, R1 = Resistor 1, R2 = Resistor 2. Type help for commands."
    )
    while True:
        isrt = input("VDC: ")
        if isrt == "help":
            print(
                "Type 'c <Vin> <Vout> <R2>' (everything in '< >' is a value you must set. Int only) to calculate R1 for a Voltage divider. Type 'exit' to leave."
            )
        elif isrt == "exit":
            break
        elif isrt.startswith("c "):
            v = isrt.split(maxsplit=3)
            Vin = int(v[1])
            Vout = int(v[2])
            R2 = int(v[3])
            print("R1 = " + str(R2 * (Vin / Vout - 1)))
