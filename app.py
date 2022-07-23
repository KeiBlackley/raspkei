from datetime import datetime
from lxml import html
import urllib3, os, configparser, subprocess, platform
import core.display

def isUpdated():
    global version
    
    try:
        # Gets <version>VERSION</version> from url
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://www.35.244.98.210/version.txt')
        data_string = r.data.decode('utf-8', errors='ignore')
        tree = html.fromstring(data_string)
        onlineVersion = tree.iter('version').text
    except:
        onlineVersion = "unknown"
        print("\n[ "+core.display.tred+"Error"+core.display.twhite+" ] Could not find online version.")
    
    # Gets VERSION from config.ini
    if (os.path.isfile("core/cfg/about.ini")):
        config = configparser.ConfigParser()
        config.read("core/cfg/about.ini")
        localVersion = config['about']['version']
        version = localVersion
        
        if (localVersion == onlineVersion):
            return True
        else:
            print("\n[ "+core.display.tred+"Error"+core.display.twhite+" ] App version is outdated.")
            return False
    else:
        localVersion = "unknown"
        print("\n[ "+core.display.tred+"Error"+core.display.twhite+" ] Could not find local version.")
        return False

def runUpdate():
    print(platform.system())
     
try:
    startTime = datetime.now()
    
    if __name__ == "__main__":
        core.display.clearScreen()
        core.display.getLogo()
        if (isUpdated()):
            core.main.start()
        else:
            runUpdate()
    else:
        print("Importing app")
        
    endTime = datetime.now()
    print("\n"+core.display.tyellow+"Runtime of:    "+core.display.twhite+str(endTime-startTime))
except KeyboardInterrupt:
	print("\nKeyboard Interrupted")
	exit()