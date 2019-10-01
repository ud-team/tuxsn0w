#Tuxsn0w, a freshsn0w alternative for *GNU+*Linux by UD-Team. Oh and it should work on the overpriced machines with a fruit on the back.

from easygui import *
import subprocess

title = "Tuxsn0w, by UD-Team"

def pwnDFU():
    subprocess.call(["ipwndfu/ipwndfu", "-p"])
    msg = "Have I PWNed your DFU? If so YAY! if not try again... Check you are actually in DFU mode and connected to this PC."
    msgbox(msg, title)

def ipswRestore():
    msg = "NOTE: THIS FEATURE IS UNTESTED! YOUR iDEVICE MAY NO LONGER BOOT AFTER THE RESTORE! ALL DATA ON YOUR iDEVICE WILL BE LOST!"
    msgbox(msg, title)
    msg = "Select your IPSW"
    ipsw = fileopenbox(msg, title)
    print(ipsw)
    if ipsw.endswith('.ipsw'):
        msg="Beginning restore"
        msgbox(msg, title)
        #subprocess.call(["idevicerestore", "-e", "-c", ipsw])
        msg="Done!"
        msgbox(msg, title)
    else:
        msg="Not an IPSW!!! Going back home..."
        msgbox(msg, title)

def main():
    while True:
        msg ="How would you like to PWN your iPhone?"
        choices = ["PWN my DFU (uses ipwndfu)", "Restore Custom IPSW", "Exit"]
        choice = buttonbox(msg, title, choices)

        if choice == "PWN my DFU (uses ipwndfu)":
            pwnDFU()

        if choice == "Exit":
            msg="Thanks for using Tuxsn0w. See you the next time you run out of charge :D!"
            msgbox(msg, title)
            break

        if choice == "Restore Custom IPSW":
            ipswRestore()


main()
