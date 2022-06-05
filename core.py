#! usr/bin/env python3
 
# File: core.py

import os
import time 
import platform
from platform import system
import pyfiglet
import termcolor
from termcolor import colored


def clear_terminal():
    if system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def splashscreen_ccake():
    clear_terminal()

    print("====================")
    print("| Welcome to Ccake |")
    print("|                  |")
    print("| Made by potato_  |")
    print("| for Developers   |")
    print("====================")

    time.sleep(3)
    clear_terminal()