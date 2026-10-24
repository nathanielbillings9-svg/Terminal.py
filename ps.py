from dve import dve
from vdc import vdc
from headlines import headline as hl

def start(programm):
    if programm == "dve":
        hl("DVE, Data and Value Editor", True)
        dve()
    elif programm == "vdc":
        hl("VDC, Voltage Divider Calculator", True)
        vdc()
    else:
        print("Unkown Programm")