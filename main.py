#! usr/bin/env python3
 
# File: main.py

import core
import time
import os
import platform
   
try:
    import pyfiglet
    from termcolor import colored
    import emoji
    print("[>] Requirements installed.")
    print("[>] Version 1.0")

except ImportError:
    print("It looks like the following package(s) are not installed yet, don't worry they will install now...")
    print("")
    print("Packages: termcolor, pyfiglet, emoji")
    time.sleep(2)
    print("")
    print("")
    os.system("pip3 install termcolor")
    os.system("pip3 install pyfiglet")
    os.system("pip3 install emoji")
    print("Requirements installed, good luck developing you app.")
    time.sleep(5)
    from termcolor import colored
    import pyfiglet
    import emoji
    runtime()

### All Ccake functions    

def ascii_generator1():

    core.clear_terminal()
    print("<< Ascii art generator, font = SLANT")
    print("")

    ascii_art1 = input("Name to convert to ascii art: ")
    artwork1 = pyfiglet.figlet_format(ascii_art1, font = "slant")
    print(artwork1)
    time.sleep(5)
    menu_bar()


def ascii_generator2():

    core.clear_terminal()
    print("<< Ascii art generator, font = DEFAULT")
    ascii_art2 = input("Name to convert to ascii art: ")
    artwork2 = pyfiglet.figlet_format(ascii_art2)
    print(artwork2)
    time.sleep(5)
    menu_bar()

def banner():
    print("""

   ______           __      
  / ____/________ _/ /_____ 
 / /   / ___/ __ `/ //_/ _ \  v1.0          
/ /___/ /__/ /_/ / ,< /  __/
\____/\___/\__,_/_/|_|\___/ 
""")
    print(emoji.emojize("Made with :red_heart: for developers"))


def menu_bar():
    print(colored("[!] Commands are case sensitive.", 'red'))
    print("")
    print("[working] 'ascii-1' to convert text to ascii (Font = Slant")
    print("[working] 'ascii-2' to convert text to ascii (Font = Default)")
    print("[Beta] 'c-comp-install' Install C compiler for your OS")
    print("[Beta] 'cpp-comp-install' Install C++ compiler for your OS")
    print("")
    print("┌─[What would you like to do?]")
    Command_Ccake = input("└──╼ ")

    if Command_Ccake == ("ascii-1"):
        print("Opening Ascii art generator...")
        time.sleep(3)
        ascii_generator1()

    elif Command_Ccake == ("ascii-2"):
        print("Opening Ascii art generator...") 
        time.sleep(3)
        ascii_generator2()
    
    elif Command_Ccake == ("c-comp-install"):
        print(emoji.emojize("Function still in development. sorry :sad_but_relieved_face:"))
        menu_bar()

    elif Command_Ccake == ("cpp-comp-install"):
        print(emoji.emojize("Function still in development. sorry :sad_but_relieved_face:"))
        menu_bar()

    else:
        print(colored("Oops, this command doen't seems to be valid, check your input and try again.", 'red'))
        print("")
        print("")
        menu_bar()


    
def runtime():
    core.splashscreen_ccake()
    banner()
    menu_bar()

runtime()
