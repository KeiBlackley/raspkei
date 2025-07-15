from termcolor import colored
import argparse, os

from core.display import printLogo
from core.installs import *

def main():
    parser = argparse.ArgumentParser(description="Raspkei")

    parser.add_argument("-w", "--wifi", action="store_true", help="Install RaspAP (WiFi Access Point)")
    parser.add_argument("-p", "--portal", action="store_true", help="Install nodogsplash (WiFi Access Portal)")

    args = parser.parse_args()

    if args.wifi:
        install_raspap()
    if args.portal:
        install_nodogsplash()
    else:
        print(colored("\nNo arguments set.", "red"))

if __name__ == "__main__":
    printLogo()
    main()