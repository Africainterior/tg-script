#!bin/env python3 ONLY
# Coded by Ahadu, Ethiopia

# COPYRIGHT 2021;

import os
import sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def banner():
    print(gr+"              __                                                      ")
    print(gr+"   ________  / /___  ______                           ")
    print(gr+"  / ___/ _ \/ __/ / / / __ \                               ")
    print(re+" (__  )  __/ /_/ /_/ / /_/ /                                 ")
    print(re+"/____/\___/\__/\__,_/ .___/                        ")
    print(re+"                   /_/                                                ")

    print("                                                     ")
    print(cy+"  Version: 3.2                               ")
    print(gr+" Made by Ahadu, Ethiopia              ")
banner()
print(gr+"Intalling useful libraries...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()    
os.system('touch config.data')
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[-] Enter api_id: "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[-] Enter api_hash: "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[-] Enter phone number: "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"You activate the hack successfuly.")
print(re+"This code is written by Ahadu, Ethiopia")
print(gr+"You can run any tool you want know :)")