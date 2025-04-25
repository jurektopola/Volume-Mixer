# Hardware volume mixer for windows

This project uses Arduino Uno controller to manipulate volume of selected programs in windows.

File `arduino_encoder.ino` contained in `ARDUINO` folder should be copied to the Arduino board, and is responsible for reading and encoding the information from potentiometers.
`main.pyw` (.pyw runs program by python without using IDE), `decode.py` and `apps.py` are responsible for manipulating the volume on Windows side.

# Mixer run
Arduino should run, when connected to power.

You need to have python installed. Connect Arduino Uno by USB (with data transfer) to your PC.
You can enable autostart for this shortcut to automatically run software when starting your PC.
1. Create shortcut to `main.pyw`
2. `Win + R`, type `shell:startup` and run
3. Move shortcut to `Start-Up` folder

# How to select applications?
To change controlled applications go to `apps.py`, change elements in list as the comments instruct.
