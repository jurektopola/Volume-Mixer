# Hardware volume mixer for windows

This project uses Arduino Uno controller to manipulate volume of selected programs in windows.

File `arduino_encoder.ino` contained in `ARDUINO` folder should be copied to the Arduino board, and is responsible for reading and encoding the information from potentiometers.
`main.py` and `decode.py` are responsible for manipulating the volume on Windows side.