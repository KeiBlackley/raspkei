def checkUpdate():
    global version
    
    try:
        # Gets <version>VERSION</version> from url
        http = urllib3.PoolManager()
        r = http.request('GET', 'https://keiblackley.github.io/version.txt')
        data_string = r.data.decode('utf-8', errors='ignore')
        tree = html.fromstring(data_string)
        onlineVersion = str(tree.xpath('//version')[0].text)

        print("[ "+core.display.tblue+"Info"+core.display.twhite+" ] Online version: " + onlineVersion)
    except Exception as e:
        print(e)
        onlineVersion = "onlineUnknown"
        print("\n[ "+core.display.tred+"Info"+core.display.twhite+" ] Could not find online version.")
    
    # Gets VERSION from config.ini
    if (os.path.isfile("core/cfg/about.ini")):
        config = configparser.ConfigParser()
        config.read("core/cfg/about.ini")
        localVersion = config['about']['version']
        version = localVersion
        
        if (localVersion == onlineVersion):
            print("[ "+core.display.tblue+"Info"+core.display.twhite+" ] Local version: " + localVersion)
            return True
        else:
            print("[ "+core.display.tblue+"Info"+core.display.twhite+" ] Local version: " + localVersion)
            print(core.display.tyellow+"To apply update run `python3 app.py update`"+core.display.twhite)
            return False
    else:
        localVersion = "localUnknown"
        print("\n[ "+core.display.tred+"Error"+core.display.twhite+" ] Could not find local version.")
        return False

def runUpdate():
    print("\n[ "+core.display.tyellow+"Info"+core.display.twhite+" ] Installing update..")
    
def main():
    core.display.clearScreen()
    core.display.printLogo()
    checkUpdate()
    core.main.start()

try:
    # Imports
    from datetime import datetime
    from lxml import html
    import urllib3, os, configparser, platform, subprocess, sys
    import core.display, core.main


    startTime = datetime.now()
    
    if __name__ == "__main__":
        if (len(sys.argv) == 1):
            main()        
        elif (len(sys.argv) == 2):
            param = sys.argv[1]
            if (param == "update"):
                runUpdate()
            elif (param == "info"):
                core.display.printInfo()
            else:
                core.display.printHelp()
        else:
            core.display.printHelp()

    endTime = datetime.now()
    print("\n"+core.display.tyellow+"Runtime of:    "+core.display.twhite+str(endTime-startTime))
except ImportError as e:
    import os
    print("\nThere was an import error, trying to download required imports...")
    os.system("python3 -m pip install lxml")
    print("\nYou can now restart.")
    print("Please restart script.")
except KeyboardInterrupt:
	print("\nKeyboard Interrupted")
	exit()