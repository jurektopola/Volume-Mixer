# Hardware volume mixer for windows

This project uses Arduino Uno controller to manipulate volume of selected programs in windows.

File `arduino_encoder.ino` contained in `ARDUINO` folder should be copied to the Arduino board, and is responsible for reading and encoding the information from potentiometers.
`main.pyw`, `decode.py` and `apps.py` are responsible for manipulating the volume on Windows side.

# How to select applications?
To change controlled applications go to `apps.py`, change elements in list as the comments instruct.

# Mixer run
You need to have python installed. Connect Arduino Uno by USB (with data transfer) to your PC. Create shortcut to `main.pyw` (.pyw runs program by python without using IDE). You can enable autostart for this shortcut to automatically run software when starting your PC.

Arduino should run, when connected to power.