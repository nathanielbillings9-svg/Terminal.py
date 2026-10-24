index = "index.txt"
File = "data.txt"
free = "FREE"
sinfo = "sysinfo.txt"
sinfoindex = {
"version" : 0
}


def write(name, data):
    f = open(index, "r+")
    l = f.readlines()
    rl = None
    for lr in l:
        if lr.startswith(free + " "):
            il = lr[len(free):]
            rl = int(il)
            l[rl] = name + " " + str(rl) + "\n"
            f.seek(0)
            f.writelines(l)
            f.truncate()
            break
    f.close()
    if rl is None:
        f = open(index, "a+")
        f.seek(0)
        l = f.readlines()
        f.write(name + " " + str(len(l)) + "\n")
        f.close()
        f = open(File, "a")
        f.write(data + "\n")
        f.close()
    else:
        f = open(File, "r+")
        l = f.readlines()
        l[rl] = data + "\n"
        f.seek(0)
        f.writelines(l)
        f.truncate()
        f.close()


def read(name):
    f = open(index, "r")
    l = f.readlines()
    rl = None
    for lr in l:
        if lr.startswith(name + " "):
            il = lr[len(name):]
            rl = int(il)
            break
    f.close()
    if rl is None:
        return None
    f = open(File, "r")
    l = f.readlines()
    o = l[rl].strip()
    f.close()
    return o


def change(name, data):
    f = open(index, "r")
    l = f.readlines()
    rl = None
    for lr in l:
        if lr.startswith(name + " "):
            il = lr[len(name) :]
            rl = int(il)
            break
    f.close()
    if rl is None:
        return None
    f = open(File, "r+")
    l = f.readlines()
    l[rl] = data + "\n"
    f.seek(0)
    f.writelines(l)
    f.truncate()
    f.close()


def delete(name):
    f = open(index, "r+")
    l = f.readlines()
    rl = None
    for lr in l:
        if lr.startswith(name + " "):
            il = lr[len(name) :]
            rl = int(il)
            l[rl] = "FREE " + str(rl) + "\n"
            f.seek(0)
            f.writelines(l)
            f.truncate()
            break
    f.close()
    if rl is None:
        return None
    f = open(File, "r+")
    l = f.readlines()
    l[rl] = "FREE\n"
    f.seek(0)
    f.writelines(l)
    f.truncate()
    f.close()


def show(mode):
    if mode == "d":
        f = open(File, "r")
        l = f.readlines()
        f.close()
    elif mode == "i":
        f = open(index, "r")
        l = f.readlines()
        f.close()
    return l


def file(mode):
    if mode == "i":
        return index
    elif mode == "d":
        return File


def getsysinfo(sinfoname):
    if sinfoname not in sinfoindex:
        return None
    f = open(sinfo, "r")
    l = f.readlines()
    f.close()
    return l[sinfoindex[sinfoname]]