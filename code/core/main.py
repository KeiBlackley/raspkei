from termcolor import colored
from datetime import datetime, timedelta
import sys, time, os, configparser, urllib3
import core.display

def is_root():
    return os.geteuid() == 0

def start():
    print("\nWhich process do you want to start?")
    print("\n")
    print("[1]		timer")
    if (input("> ") == "1"):
    	print("Starting timer...")
    else:
    	print("Invalid reponse!")

def exit():
	print("[ "+core.display.tblue+"Raspkei"+core.display.twhite+" ] Terminating script.\n")	
	sys.exit()

def getVersion(onlineYes):
	if (onlineYes == 0):
	    if (os.path.isfile("core/cfg/about.ini")):
	        config = configparser.ConfigParser()
	        config.read("core/cfg/about.ini")
	        return config['about']['version']
	else:
		http = urllib3.PoolManager()
		r = http.request('GET', 'https://keiblackley.github.io/version.txt')
		data_string = r.data.decode('utf-8', errors='ignore')
		tree = html.fromstring(data_string)
		return str(tree.xpath('//version')[0].text)
		
def askQuestion(msg, colour, default_yes = False):
	print("\n")
	print(colored(msg, colour), end = "")
	given = ""
	valid =  False
	while not valid:
		if default_yes:
			given = input(colored(" [Y/n] \n", colour))
			if not given:
				given = "y"
		else:
			given = input(colored(" [y/N] \n", colour))
			if not given:
				given = "n"
			
		if given.lower() in ["y", "yes"]:
			return True
		elif given.lower() in ["n", "no"]:
			return False
		else:
			print(colored("Invalid user input. [y/n] only.\n", "red")) 
    
def askInput(msg, colour):
    while True:
        try:
            user_input = input(msg + ": ")
            user_input = str(user_input)

            if user_input and user_input.isalnum():
                return user_input
            else:
                print(colored("Invalid user input.\n", "red"))

        except Exception as e:
            print(colored(f"An unexpected error occurred: {e}", "red"))


def wait():
    config = configparser.ConfigParser()
    config.read("core/cfg/config.ini")
    last_switched = config['light']['last_switched']
    lightstatus = config['light']['lightstatus']

    if (lightstatus == "1"):
        print("status on")
    elif (lightstatus == "0"):
        print("status off")
    else:
        print("[ "+core.display.tred+"Error"+core.display.twhite+" ] Light Status does not exist.")	

def switch():	
	config = configparser.ConfigParser()
	config.read("core/cfg/config.ini")
	status = config['light']['lightstatus']
	if status == "0": 
		pos = 1;
	else:
		pos = 0

	print("\n[ "+core.display.tblue+"Light"+core.display.twhite+" ] Switched light to `"+core.display.tblue+str(pos)+core.display.twhite+"`. @ " +core.display.tblue+ str(datetime.now()) +core.display.twhite)
	time.sleep(1)
	config.set('light', 'last_switched', str(datetime.now()))
	config.set('light', 'lightstatus', str(pos))
	with open("cfg/config.ini", 'w') as configfile:
	    config.write(configfile)
    
def timer():
	if (os.path.isfile("cfg/config.ini")):
		print("\n[ "+core.display.tblue+"Raspkei"+core.display.twhite+" ] Started waiting...")
		print("\nRunning until exit. Waits until current time is less than `last_switched` to switch data.")
		while True:
			wait()
	else:
		print("[ "+core.display.tred+"Error"+core.display.twhite+" ] Could not find `"+core.display.tred+"cfg/config.ini"+core.display.twhite+"`.")	
		print("[ "+core.display.tblue+"Raspkei"+core.display.twhite+" ] Waiting to be created via web. Checking every 10 seconds...")	
		time.sleep(10)
		timer()