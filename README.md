dso6014a.py --> RPi (pyvisa and pyvisa-py, spidev, RPi.GPIO soon)

main.py --> Windows (paramiko)

Windows SSH is setup with authkeys and no password. 

Change ID in dso6014a.py to match VISA address of test instrument. Probably won't work with modern Windows Keysight equipment due to a frequent complaint regarding usbtmc.py problems on the RPi.

Please add ssh-info.txt in the main.py directory and add SSH host IP on the first line and the ssh username on the second line.
