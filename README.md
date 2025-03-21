# EDD Frequency Control

![Python Compile](https://github.com/AlexChapin/EDDFrequencyControl/actions/workflows/pythoncompile.yml/badge.svg)

Simple application to create a tone and play it from system speakers.

## Description

Plays two frequencies concurrently through system speakers. Allows setting of 5 preset frequencies and startup frequencies along with inputs for custom on the fly frequency generation. Also has an automatic mode where the frequency will be changed through presets that can be configured by the user. 

### Dependencies

Requires Packages:
cffi
colorzero
gpiozero
numpy
pigpio
pillow
pycparser
pysinewave
setuptools
sounddevice

### Installing

Install Python 11, 12 or 13
Navigate to Program Location
Use Git or Download Latest Release
Navigate to Where the Software is Located
```
cd /path/to/EDDFrequencyControl
```

Create a venv Environment
```
python -m venv /path/to/EDDFrequencyControl
```

Activate venv Environment
Linux:
```
source bin/activate
```
Windows:
```
.\venv\Scripts\activate.bat
```

Use Pip to Install Dependencies
```
Pip install -r requirements.txt
```

### Executing program

* To execute the program simply run Main.py

* To run the programmed set of frequencies run Main.py with the -auto flag or change the value "runmanual" in Main.py

Windows:
```
& 'Path To Python Interpreter' 'Path to Main.py'
```

Linux: (With Venv Activated)
```
python main.py
```

## Accepted Startup Flags

* -a, -auto, -automatic -> Runs the Program in Automatic Mode

* -m, -man, -manual -> Runs the Program in Manual Mode

* elise -> Plays a little song for Elise

## Help

Accepts any Frequency Value From 0 Hz and 20000 Hz
Accepts any Amplitude Value from 0 % to 100 %

If the program will not run check the console for errors due to setting presets incorrectly.

Exit Codes:

1 -> Too Many Flags Passed

2 -> Invalid Flags Passed

3 -> Tried to Set PWM Pin on Servo to an Invalid Pin Number

4 -> Preset Frequency Set Incorrectly

5 -> Preset Frequency Set To Non-Numerical Value

6 -> Preset Amplitude Set Incorrectly

7 -> Preset Amplitude Set To Non-Numerical Value

## Raspberry Pi Audio Issues
If a crackling sound is present in the audio stream when running on a raspberry pi modify the line
```
self.output_stream = sd.OutputStream(channels=channels, callback= lambda *args: self._callback(*args), 
         samplerate=samplerate)
```
in Lib/site-packages/pysinewave/sinewave.py to read
```
self.output_stream = sd.OutputStream(blocksize=2048, channels=channels, callback= lambda *args: self._callback(*args), 
         samplerate=samplerate)
```

If the issue persists increase the block size further to 4096 or larger.
It is not recomended to increase the block size past 8192

## Authors

Alex Chapin
[@AlexChapin](https://github.com/AlexChapin)

## Version History

* 1.1.0
    * Rutgers Release
    * Tested / Demonstrated at HUNCH CDR (2/26/25)
    * Allowed Setting of PWM Servo Pin
    * Ensured Accurate Servo Pin Setting
    * Slight Logic Changes
    * Fixed Timer Issues
* 1.0.5
    * Added Servo Control
    * Added 11 Automatic Phases
    * Reduced CPU Load Averages
    * Improved Timing Accuracy
    * Moved Configs to configs.py
    * Moved Assets to Assets Folder
    * GUI Customization
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
    * Configure Initial GUI
    * Custom Inputs
    * 2 Frequencies
    * 5 Presets / Frequency