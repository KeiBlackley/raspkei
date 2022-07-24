import subprocess, socket
import core.main

tred = "\033[31m"
tgreen = "\033[32m"
tyellow = "\033[33m"
tblue = "\033[36m"
twhite = "\033[37m"

def printLogo():
    print(tred+r""" ____                 _        _ 
|  _ \ __ _ ___ _ __ | | _____(_)
| |_) / _` / __| '_ \| |/ / _ \ |
|  _ < (_| \__ \ |_) |   <  __/ |
|_| \_\__,_|___/ .__/|_|\_\___|_|
               |_|"""+twhite+"\n")

def printInfo():  
    print("\n[ "+tblue+"Info"+twhite+" ]")
    print(tblue+"# Raspkei"+twhite)
    print(tblue+"Developer:     "+twhite+"Keirran Blackley")
    print(tblue+"Online Version:       "+twhite+core.main.getVersion(1))
    print(tblue+"Local Version:       "+twhite+core.main.getVersion(0))

    print("\n"+tblue+"# Device"+twhite)
    print(tblue+"Host:          "+twhite+socket.gethostname())
    
def printHelp():
    print("\n[ "+tyellow+"Help"+twhite+" ]")
    print("Usage: python3 run.py <command> \n")
    print("<command>            <description>\n")
    print("                     runs raspkei")
    print("help 		     outputs the list of params")
    print("update               installs a new core")
    print("info                 gets all info recorded")
    
def clearScreen():
    subprocess.call("cls", shell=True)
    subprocess.call("clear", shell=True)
