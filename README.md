dso6014a.py --> RPi (pyvisa and pyvisa-py, spidev, RPi.GPIO soon) \n
main.py --> Windows (paramiko) \n

Windows SSH is setup with authkeys and no password. \n
Change ID in dso6014a.py to match VISA address of test instrument. Probably won't work with modern Windows Keysight equipment due to a frequent complaint regarding usbtmc.py problems on the RPi. \n

Please add ssh-info.txt in the main.py directory and add SSH host IP on the first line and the ssh username on the second line.
