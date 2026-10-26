def calculator():
    print("Math operations you can do: +, -, *, /\nType 'exit' to leave\n")
    while True:
        x = input("Calculator: ")
        if x == "exit":
            break
        if all(c in "0123456789.+-*/ " for c in x):
            print(eval(x))
        else:
            print(
                "Invalid User input: '"
                + x
                + "' allowed symbols are: '0123456789.+-*/ '"
            )
