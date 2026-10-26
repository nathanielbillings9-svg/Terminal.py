import time
import random
import os

menu = ["1. Terminal.py", "2. end"]
print("\n" * 2)
print("\n".join(menu))

bo = input("").strip()

if bo == "1":
    scv = "V2"
    print("Checking dama.py...")
    time.sleep(random.uniform(0.3, 1.2))
    import dama

    print("dama.py [OK]")
    print("Checking headlines.py...")
    time.sleep(random.uniform(0.3, 1.2))
    import headlines

    print("headlines.py [OK]")
    print("Checking dve.py...")
    time.sleep(random.uniform(0.3, 1.2))
    import dve

    print("dve.py [OK]")
    print("Checking dv.py...")
    time.sleep(random.uniform(0.3, 1.2))
    import dv

    print("dv.py [OK]")
    print("Checking calc.py...")
    time.sleep(random.uniform(0.3, 1.2))
    import calc

    print("calc.py [OK]")
    print("Checking vdc.py...")
    time.sleep(random.uniform(0.3, 1.2))
    import vdc

    print("vdc.py [OK]")
    print("Checking ps.py...")
    time.sleep(random.uniform(0.3, 1.2))
    import ps

    print("ps.py [OK]")
    print("Checking Terminal.py...")
    time.sleep(random.uniform(0.3, 1.2))
    import Terminal

    print("Terminal.py [OK]")
    print("-" * 20)
    print("Simple Check " + scv)

    size = os.path.getsize("Terminal.py")
    print("Getting Terminal.py size...")
    time.sleep(random.uniform(3.2, 5.6))
    print("Terminal.py size: " + str(size))

    size_check = input('Do the size check? (y/n) [default: y]: ').strip().lower()
    if size_check in ("", "y"):
        if size + 86 in (900, 934):
            print("File Size check successful, booting now...")
        else:
            print("File Size check failed. Continuing anyway because it's just a fun check, not a real security feature.")
    elif size_check == "n":
        print("Ignoring size check. Continuing because it's just a fun feature.")
    else:
        print("Invalid choice. Defaulting to ignore the size check.")

    time.sleep(random.uniform(4.7, 10.4))
    print("")
    print("-------------------------------")
    print("Terminal.py")
    print("Version: " + dama.getsysinfo("version"))
    print("-------------------------------")
    print("")

    Terminal.terminal()

    print("\nThank You for using Terminal.py, bye :)")
elif bo == "2":
    print("Exiting...")
    print("Bye :)")
else:
    print("Invalid option. Please choose 1 or 2.")
