#!usr/bin/env/python

import os
import time

Y = set(['yes', 'y', 'YES' ,'Y'])
N = set(['no', 'n' ,'NO', 'N'])

os.system("figlet INSTALLATION")
print("This tool needs some depedencies")
agree = input("Do you want to install them Y / N ")

def dependent():
    if agree in Y:
        print("INSTALLING")
        os.system("sudo apt-get update")
        os.system("sudo apt-get install figlet")
        os.system("pip3 install bs4")
    elif agree in N:
        print("This required mandatory depedencies")
        exit()
dependent()
