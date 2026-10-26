import dama
import ps

cmds = "exit, help, start, get"

if __name__ == "__main__":
    tname = "main"
else:
    tname = __name__


def terminal():

    if dama.read("user") is None:
        username = input("enter username: ")
        dama.write("user", username)
    username = dama.read("user")

    while True:
        cmd = input(username + "@" + tname + ": ")
        if cmd == "exit":
            break
        elif cmd == "help":
            print(str(cmds))
        elif cmd.startswith("get "):
            si = dama.getsysinfo(cmd[4:])
            if si is None:
                print("The system info '" + str(cmd[4:]) + "' was not found")
            else:
                print(si)
        elif cmd.startswith("start "):
            ps.start(cmd[6:])
        else:
            print("command unknown")
