# RPi-eink-display

This project uses a Pimoroni Inky 7 color e-ink display to intermittantly display an image using a Raspberry Pi zero. I use this to display my Son's artwork but it could be used for anything which requires an image to be displayed and refreshed at relativley long (>1hr) intervals.

Everything is enclosed in a single picture frame and battery powered, with integrated charging via a TP4056.

The Raspberry Pi is normally off and is triggered to activate using an Adafruit external timer IC. There are cheaper ways of doing this but this is probably the easiest and doesnt even require a PCB - I just built it on perfboard.

## Software
The images are stored on a seperate Samba-share. This allows you to upload images anytime and they are readily available. I host them on a seperate Raspberry pi. There are 2 ways to implement this project:

1) Build and run the included Dockerfile. At the time of writing I lost patience with this as I could not get it to work properly. But in theory it should mount the SMB drive automatically and run the code. I will update this section if/when I get it to work.

2) Clone this repo to the pi zero and do the following:
* Pip install -r requirements.txt
* Mount your SMB share to the pi in the /etc/fstab file. Set the mount point to '/mnt/pi_smb' 
* Create a cronjob to run the launcher.sh script at boot

## Hardware
You will need the following:
* Pimoroni inky display. I use the 7.3" version but others should work (with possible modifications to the display setuup in the 'cycle_images.py' script.
* TP4056 lithium charger IC.
* Li-ion to 5v boost converter. I used a cheap one from ebay.
* Adafruit TPL5110 Low Power Timer Breakout.
* Li-ion battery/batteries. I used found batteries reclaimed from disposable e-cigarettes (you can literally find them on the street).
* Some perfboard.

I have included some images and a hookup diagram. This one is relativley simple to assemble.
