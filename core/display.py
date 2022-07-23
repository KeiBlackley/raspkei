import subprocess, socket
import core.main

tred = "\033[31m"
tgreen = "\033[32m"
tyellow = "\033[33m"
tblue = "\033[36m"
twhite = "\033[37m"

def getLogo():
    print(tred+r""" ____                 _        _ 
|  _ \ __ _ ___ _ __ | | _____(_)
| |_) / _` / __| '_ \| |/ / _ \ |
|  _ < (_| \__ \ |_) |   <  __/ |
|_| \_\__,_|___/ .__/|_|\_\___|_|
               |_|"""+twhite+"\n")

def getInfo():  
    subprocess.call("cls", shell=True)
    subprocess.call("clear", shell=True)
    print(tblue+"Developer:     "+twhite+"Keirran Blackley")
    print(tblue+"Version:       "+twhite+core.main.getVersion())

    print("\n"+tblue+"Host:          "+twhite+socket.gethostname())
    
def printHelp():
    print(tyellow+"### HELP ###"+twhite)
    print("Usage: python3 run.py <command> \n")
    print("<command>		<description>\n")
    print("help 			outputs the list of commands")
    
    
def clearScreen():
    subprocess.call("cls", shell=True)
    subprocess.call("clear", shell=True)
