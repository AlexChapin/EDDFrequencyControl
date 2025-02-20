# EDD Frequency Control

![Python Compile](https://github.com/AlexChapin/EDDFrequencyControl/actions/workflows/pythoncompile.yml/badge.svg)

Simple application to create a tone and play it from system speakers.

## Description

Plays two frequencies concurrently through system speakers. Allows setting of 5 preset frequencies and startup frequencies along with inputs for custom on the fly frequency generation. Also has an automatic mode where the frequency will be changed through presets that can be configured by the user. 

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
Pip install -r requirements.txt
```

### Executing program

* To execute the program simply run Main.py

* To run the programmed set of frequencies run Main.py with the -a flag or change the value "runmanual" in Main.py 

Windows:
```
& 'Path To Python Interpreter' 'Path to Main.py'
```

## Help

Accepts any Frequency Value From 0 Hz and 20000 Hz
Accepts any Amplitude Value from 0 % to 100 %

If the program will not run check the console for errors due to setting presets incorrectly.

Exit Codes:

1 -> Too Many Flags Passed

2 -> Invalid Flags Passed

3 -> Tried to Run Configs.py

4 -> Preset Frequency Set Incorrectly

5 -> Preset Frequency Set To Non-Numerical Value

6 -> Preset Amplitude Set Incorrectly

7 -> Preset Amplitude Set To Non-Numerical Value

## Authors

Alex Chapin
[@AlexChapin](https://github.com/AlexChapin)

## Version History

* 1.0.4
    * Added Automatic Operation Mode
    * 4 Preset Modes in Automatic
    * Changed Amplitude Calculation to Base10
    * Modified Frequency Changes
    * Reduced Required CPU Load
    * Added Startup Flags
    * Created Auto GUI
    * Added OS Checking
* 1.0.3
    * Added Sweep Mode
    * Added Frequency Sliders
    * Added Frequency Slider Menu
    * GUI Changes
    * Frequency Transition Changes
    * Corrected Button Behavior
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

