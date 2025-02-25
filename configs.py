# User Input
# Dertermines Whether to Start the Program to Accept Manual Inputs or Run a Preset Program
# True Means Enable User Inputs
# False Means Run Preprogramed Routine
# This Value Will Be Overwritten by Any Startup Flags
runmanual = True

# Default Frequency On Startup
startupfreq1 = 0  # Hz
startupamp1 = 0  # Percent

startupfreq2 = 0  # Hz
startupamp2 = 0  # Percent

# Frequency 1 Settings
setting1freq = 15  # Hz
setting1amp = 75  # Percent

setting2freq = 16.5  # Hz
setting2amp = 45  # Percent

setting3freq = 17.5  # Hz
setting3amp = 50  # Percent

setting4freq = 19  # Hz
setting4amp = 70  # Percent

setting5freq = 45  # Hz
setting5amp = 100  # Percent

# Frequency 2 Settings
setting1freq2 = 5  # Hz
setting1amp2 = 100  # Percent

setting2freq2 = 15  # Hz
setting2amp2 = 75  # Percent

setting3freq2 = 35  # Hz
setting3amp2 = 75  # Percent

setting4freq2 = 65  # Hz
setting4amp2 = 50  # Percent

setting5freq2 = 100  # Hz
setting5amp2 = 20  # Percent

# Slider Settings
freq1sliderlow = 1  # Hz
freq1sliderhigh = 100  # Hz

freq2sliderlow = 1  # Hz
freq2sliderhigh = 100  # Hz

# Smallest Unit That The Slider Can Change By
scaleresolution = 0.1  # Hz

freq1buttonpreset = 100  # Percent
freq2buttonpreset = 100  # Percent

# Sweep Rates
# Fast Sweep Rates are Default
fastsweeprate1 = 1000000000  # Pitch / Second
fastsweeprate2 = 1000000000  # Pitch / Second

slowsweeprate1 = 2  # Pitch / Second
slowsweeprate2 = 2  # Pitch / Second





# Auto Settings
autofreqsweeprate = 10000  # Pitch / Second
autoampsweeprate = 10000  # Percent / Second

# GPIO Pin to Run ServoPWM
# Acceptable Pins: 12, 13, 18, 19
gpioservopin = 12

# Include ms in Timer
dospecifictimer = False

# Servo Settings
servopos1 = 1000
servopos2 = 1250

# Settings for State 1
autofreq1 = 22  # Hz
autoamp1 = 3.5  # Percent
autotime1 = 5  # Seconds

# Settings for State 2
autofreq2 = 17.5  # Hz
autoamp2 = 2 # Percent
autotime2 = 5  # Seconds

# Settings for State 3
autofreq3 = 16  # Hz
autoamp3 = 2 # Percent
autotime3 = 5  # Seconds

# Settings for State 4
autofreq4 = 22  # Hz
autoamp4 = 3.5  # Percent
autotime4 = 5  # Seconds

# Settings for State 5
autofreq5 = 17.5  # Hz
autoamp5 = 2 # Percent
autotime5 = 5  # Seconds

# Settings for State 6
autofreq6 = 22  # Hz
autoamp6 = 3.5  # Percent
autotime6 = 5  # Seconds

# Settings for State 7
autofreq7 = 16  # Hz
autoamp7 = 2 # Percent
autotime7 = 5  # Seconds

# Settings for State 8
autofreq8 = 22  # Hz
autoamp8 = 3.5  # Percent
autotime8 = 5  # Seconds

# Settings for State 9
autofreq9 = 17.5  # Hz
autoamp9 = 2 # Percent
autotime9 = 5  # Seconds

# Settings for State 10
autofreq10 = 22  # Hz
autoamp10 = 3.5  # Percent
autotime10 = 5  # Seconds

# Settings for State 11
autofreq11 = 40  # Hz
autoamp11 = 25  # Percent
autotime11 = 5  # Seconds


if __name__ == "__main__":
    import sys
    exitcode = 3
    print("Please Run main.py Instead of configs.py!!!")
    print("Process Exited With Exit Code:" + f"{exitcode}")
    sys.exit(exitcode)