# Hardware volume mixer for windows

This project uses RaspberryPi Pico controller to manipulate volume of selected programs in windows.

Files contained in `PICO` folder should be copied to the Pico board, and are responsible for reading the information from potentiometers.
`main.py` and `read.py` are responsible for manipulating the volume on Windows side.