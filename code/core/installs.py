from termcolor import colored

from core.main import is_root

def install_raspap():
    print(colored("\nWiFi Access Point Installation using RaspAP", "cyan"))
    
    print(colored("\nInstalling RaspAP..", "yellow"))
    os.system("curl -sL https://install.raspap.com | bash -s -- --yes;")

def install_nodogsplash():
    print(colored("\nWiFi Access Portal Installation using nodogsplash", "cyan"))

    if not is_root():
        print(colored("Continuing requires elevated privileges..\n", "magenta"))
        exit(0)
    else:
        print(colored("Installing dependencies..", "yellow"))
        os.system("sudo apt-get install libmicrohttpd-dev;")
        print(colored("\nInstalling nodogsplash..", "yellow"))
        os.system("cd ~/; git clone https://github.com/nodogsplash/nodogsplash.git -y; cd nodogsplash; make; sudo make install;")

        print(colored("\nCreating nodogsplash.conf backup..", "yellow"))
        os.system("sudo mv /etc/nodogsplash/nodogsplash.conf /etc/nodogsplash/nodogsplash.conf.backup")

        print(colored("\nCreating nodogsplash.conf..", "yellow"))
        with open("/etc/nodogsplash/nodogsplash.conf", "w") as file:
            file.write(fr"""## Custom Nodogsplash Configuration for Raspkei
# Modified Configuration
GatewayInterface wlan0
WebRoot /home/skunkei/raspkei/portal
GatewayName RaspkeiAP
GatewayAddress 10.3.141.1
SplashPage login.html
            """)

            file.write(r"""# Default Configuration
        MaxClients 250
            """)
        
            file.write(r"""# Default Firewall Rules
FirewallRuleSet authenticated-users {
FirewallRule allow all
}

FirewallRuleSet preauthenticated-users {
FirewallRule allow tcp port 53
FirewallRule allow udp port 53
}

FirewallRuleSet users-to-router {
FirewallRule allow udp port 53
FirewallRule allow tcp port 53
FirewallRule allow udp port 67

FirewallRule allow tcp port 22
FirewallRule allow tcp port 80
FirewallRule allow tcp port 443
}
            """)

        print(colored("\nStarting nodogsplash..", "yellow"))
        os.system("sudo cp ~/nodogsplash/debian/nodogsplash.service /lib/systemd/system/; sudo systemctl enable nodogsplash.service; sudo systemctl start nodogsplash.service;")