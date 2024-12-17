# EDD Frequency Control

Simple application to create a tone and play it from system speakers.

## Description

Plays two frequencies concurrently. Allows setting of 5 Presets at the top of the Main.py file. Also has custom frequency inputs for each frequencies.

### Dependencies

Requires Packages:
cffi
numpy
pillow
pycparser
pysinewave
sounddevice

### Installing

Install Python 12 or 13
Navigate to Program Location
Use Pip to Install Dependencies

```
Pip install requirements.txt
```

### Executing program

* To Execute the program simply run Main.py

Windows:
```
& 'Path To Python Interpreter' 'Path to Main.py'
```

## Help

Accepts any Frequency Value From 1 Hz and 20000 Hz
Accepts any Amplitude Value from 0 % to 100 %

If the program will not run check the console for errors due to setting presets incorrectly.

Exit Codes:

10 -> Preset Frequency Set Incorrectly
11 -> Preset Frequency Set To Non-Numerical Value
12 -> Preset Amplitude Set Incorrectly
13 -> Preset Amplitude Set To Non-Numerical Value

## Authors

Alex Chapin
[@AlexChapin](https://github.com/AlexChapin)

## Version History

* 1.0.2
    * Checking of Preset Values
    * Normalized Values
    * Customized GUI
    * GUI Fixes
    * Full OS Integration
    * Added Exit Handling
* 1.0.1
    * GUI Reskin
    * String Error Catching
    * Refinement of Frequency Change
* 1.0.0
    * Initial Release
    * Intial Frequency Functionality

