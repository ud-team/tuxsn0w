#Tuxsn0w, a freshsn0w alternative for *GNU+*Linux by UD-Team. Oh and it should work on the overpriced machines with a fruit on the back.

import sys
import subprocess

try:
    from easygui import *
except:
    print("ERROR: The \"easygui\" module is not installed, please download it from https://pypi.org/project/easygui/#files .")
    sys.exit(0)


title = "Tuxsn0w - by UD-Team"

def pwnDFU():
    subprocess.call(["ipwndfu/ipwndfu", "-p"])
    msg = "DFU should be PWNed. If reconnect you device and try again."
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

def demote():
    msg = "DANGER! DEMOTING YOUR DEVICE MAY RESULT IN UNFORESEEN SIDE EFFECTS! PROCEED WITH CAUTION!"
    choices = ["Continue", "Abort"]
    choice = buttonbox(msg, title, choices)
    if choice == "Continue":
        subprocess.call(["ipwndfu/ipwndfu", "--demote"])
        msg = "Device demoted!"
        msgbox(msg, title)

def main():
    while True:
        msg = "Welcome to Tuxsn0w!\nPlease select your desired use with the buttons below.\n\nPlease also make sure your iDevice is connected to your computer."
        choices = ["PWN my DFU (uses ipwndfu)", "Restore Custom IPSW", "Demote device (DANGEROUS)", "Exit"]
        choice = buttonbox(msg, title, choices)

        if choice == "PWN my DFU (uses ipwndfu)":
            pwnDFU()

        if choice == "Restore Custom IPSW":
            ipswRestore()

        if choice == "Demote device (DANGEROUS)":
            demote()

        if choice == "Exit":
            break


main()
