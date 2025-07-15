# Raspkei
This project was made using a `Raspberry Pi 3b+`. Tested on `Raspberry Pi OS Lite (64-bit)`.
Made for educational purposes only.

## Table of Contents
* [Hardware](#hardware)
* [Raspberry Pi Setup](#raspberry-pi-setup)
* [WiFi Hotspot](#wifi-hotspot)

---

## Hardware
You will need:
- A Raspberry Pi (with built in wifi capabilities)
    - microSD Card [*boot media*]
- Ethernet cable (for ssh)
- Laptop or computer with Ethernet Port (for ssh)

---

## Raspberry Pi Setup
### Install Raspberry Pi OS using Raspberry Pi Imager
Download and Run [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
Select your:
1. **Device** [*made with* **Raspberry Pi 3***b+*]
2. **Operating System** [*tested on* **Raspberry Pi OS Lite (64-bit)**]
3. **Storage** [*Pi boot media* **microSD Card**]

Apply OS customisation settings:
- **General**
    - **HOSTNAME** [*custom or to suit: raspkei*]
    - Login credentials [*enter* **USERNAME** *and* **PASSWORD**]
    - Set locate settings
- **Services**
    - Enable SSH *using* password authentication

Save and Continue.

After a sucessful write of Raspberry Pi OS, you can now:
1. Attach your *Pi boot media* to your Pi
2. Connect the Pi to your laptop or computer via an Ethernet cable
3. Power On the Pi
4. Wait for the device to boot.

You will now be able to ssh into your device by using your **USERNAME** and **HOSTNAME**.
```
ssh USERNAME@HOSTNAME.local;
```
### First Boot
- Update using ```sudo apt update``` and ```sudo apt full-upgrade -y```
- Use ```sudo raspi-config``` to:
    - Set **WLAN Country** in *Localisation Options* 

---

## WiFi Hotspot
Please make sure your **Pi is updated** and has **WLAN Country set** in *Localisation Options*.

### Install RaspAP
Install RaspAP with default inputs.
```bash
curl -sL https://install.raspap.com | bash -s -- --yes;
```
Login to RaspAP Access Point using default credentials:
- Visit [RaspAP's WebGUI](http://10.3.141.1) (```http://10.3.141.1```)
    - Username: ```admin```
    - Password: ```secret```
    - 
Change RaspAP default credentials
- Go to **Authentication** and change login credentials
- Go to **Hotspot > Security** to change SSID and password



## (optional) WiFi Access Portal
This step is optional after setting up your WiFi Hotspot. 
See [WiFi Hotspot](#wifi-hotspot).

### Install nodogsplash and dependencies
```bash
sudo apt-get install libmicrohttpd-dev;
cd ~/;
git clone https://github.com/nodogsplash/nodogsplash.git -y;
cd nodogsplash;
make;
sudo make install;
```

### Configure nodogsplash
```bash
sudo nano /etc/nodogsplash/nodogsplash.conf;
```
```conf
GatewayInterface wlan0
WebRoot
GatewayName RaspkeiAP
GatewayAddress 10.3.141.1
SplashPage login.html
```


### Starting nodogsplash
```bash
sudo cp ~/nodogsplash/debian/nodogsplash.service /lib/systemd/system/;
sudo systemctl enable nodogsplash.service; 
sudo systemctl start nodogsplash.service;
sudo systemctl status nodogsplash.service;
```