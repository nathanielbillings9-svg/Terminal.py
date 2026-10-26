from dv import dv
from dve import dve
from vdc import vdc
from calc import calculator as calc
from headlines import headline as hl

programms = {"dve, vdc, calc, dv"}


def start(programm):
    if programm == "list":
        print(programms)
    elif programm == "dve":
        hl("DVE", True, True, False, False)
        hl("Dama Value Editor", False, False, True, True)
        dve()
    elif programm == "vdc":
        hl("VDC", True, True, False, False)
        hl("Voltage Divider Calculator", False, False, True, True)
        vdc()
    elif programm == "calc":
        hl("CALC", True, True, False, False)
        hl("Calculator", False, False, True, True)
        calc()
    elif programm == "dv":
        hl("DV", True, True, False, False)
        hl("Dama Viewer", False, False, True, True)
        dv()
    else:
        print("Unknown Programm")
