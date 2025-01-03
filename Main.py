import numpy as np
import warnings
import sys
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from pysinewave import SineWave

# Default Frequency On Startup
startupfreq1 = 0
startupamp1 = 0

startupfreq2 = 0
startupamp2 = 0

# Frequency 1 Settings
setting1freq = 100
setting1amp = 100

setting2freq = 200
setting2amp = 100

setting3freq = 300
setting3amp = 100

setting4freq = 400
setting4amp = 100

setting5freq = 500
setting5amp = 100

# Frequency 2 Settings
setting1freq2 = 100
setting1amp2 = 100

setting2freq2 = 200
setting2amp2 = 100

setting3freq2 = 300
setting3amp2 = 100

setting4freq2 = 400
setting4amp2 = 100

setting5freq2 = 500
setting5amp2 = 100

# Slider Settings
freq1sliderlow = 1
freq1sliderhigh = 1000

freq2sliderlow = 1
freq2sliderhigh = 1000

# Smallest Unit That The Slider Can Change By
scaleresolution = 0.5

freq1buttonpreset = 100
freq2buttonpreset = 100

# Sweep Rates
# Fast Sweep Rates are Default
fastsweeprate1 = 1000000000
fastsweeprate2 = 1000000000

slowsweeprate1 = 2
slowsweeprate2 = 2

# Stores Custom Frequencies and Amplitudes to Lists for Checks
frequencies = [
    startupfreq1,
    startupfreq2,
    setting1freq,
    setting2freq,
    setting3freq,
    setting4freq,
    setting5freq,
    setting1freq2,
    setting2freq2,
    setting3freq2,
    setting4freq2,
    setting5freq2,
    freq1sliderlow,
    freq1sliderhigh,
    freq2sliderlow,
    freq2sliderhigh,
]
amplitudes = [
    startupamp1,
    startupamp2,
    setting1amp,
    setting2amp,
    setting3amp,
    setting4amp,
    setting5amp,
    setting1amp2,
    setting2amp2,
    setting3amp2,
    setting4amp2,
    setting5amp2,
    freq1buttonpreset,
    freq2buttonpreset,
]

i = 0
# Checks to Ensure Custom Frequencies are Within Valid Ranges
while i < len(frequencies):
    try:
        if frequencies[i] > 20000 or frequencies[i] < 0:
            exitcode = 10
            name = [k for k, v in globals().items() if id(v) == id(frequencies[i])][0]
            print("Error In Variable:" + name)
            print(f"{frequencies[i]}" + " Is Out Of Bounds For Frequency")
            print("Process Exited With Exit Code:" + f"{exitcode}")
            sys.exit(exitcode)
    except Exception:
        exitcode = 11
        name = [k for k, v in globals().items() if id(v) == id(frequencies[i])][0]
        print("Error in Variable:" + name)
        print("Non Numerical Inputs Not Acceptable for Type Float")
        print("Process Exited With Exit Code:" + f"{exitcode}")
        sys.exit(exitcode)
    i += 1

i = 0
# Checks to Ensure Custom Amplitudes are Within Valid Ranges
while i < len(amplitudes):
    try:
        if amplitudes[i] > 100 or amplitudes[i] < 0:
            exitcode = 12
            name = [k for k, v in globals().items() if id(v) == id(amplitudes[i])][0]
            print("Error In Variable:" + name)
            print(f"{amplitudes[i]}" + " Is Out Of Bounds For Amplitude")
            print("Process Exited With Exit Code:" + f"{exitcode}")
            sys.exit(exitcode)
    except Exception:
        exitcode = 13
        name = [k for k, v in globals().items() if id(v) == id(amplitudes[i])][0]
        print("Error in Variable:" + name)
        print("Non Numerical Inputs Not Acceptable for Type Float")
        print("Process Exited With Exit Code:" + f"{exitcode}")
        sys.exit(exitcode)
    i += 1

# Version Number:
version = "v1.0.3"

# Establish Setting Names
setting1name = (
    str(round(setting1freq, 2)) + " Hz / " + str(round(setting1amp, 2)) + "% Amplitude"
)
setting2name = (
    str(round(setting2freq, 2)) + " Hz / " + str(round(setting2amp, 2)) + "% Amplitude"
)
setting3name = (
    str(round(setting3freq, 2)) + " Hz / " + str(round(setting3amp, 2)) + "% Amplitude"
)
setting4name = (
    str(round(setting4freq, 2)) + " Hz / " + str(round(setting4amp, 2)) + "% Amplitude"
)
setting5name = (
    str(round(setting5freq, 2)) + " Hz / " + str(round(setting5amp, 2)) + "% Amplitude"
)

setting1name2 = (
    str(round(setting1freq2, 2))
    + " Hz / "
    + str(round(setting1amp2, 2))
    + "% Amplitude"
)
setting2name2 = (
    str(round(setting2freq2, 2))
    + " Hz / "
    + str(round(setting2amp2, 2))
    + "% Amplitude"
)
setting3name2 = (
    str(round(setting3freq2, 2))
    + " Hz / "
    + str(round(setting3amp2, 2))
    + "% Amplitude"
)
setting4name2 = (
    str(round(setting4freq2, 2))
    + " Hz / "
    + str(round(setting4amp2, 2))
    + "% Amplitude"
)
setting5name2 = (
    str(round(setting5freq2, 2))
    + " Hz / "
    + str(round(setting5amp2, 2))
    + "% Amplitude"
)

# Set Initial Frequencies
activefrequency1 = startupfreq1
activeamplitude1 = startupamp1
activefrequency2 = startupfreq2
activeamplitude2 = startupamp2


# GUI Global Settings
font = "Century"
tinyfontsize = 15
smallfontsize = 20
titlefontsize = 35
backgroundcolor = "#09142B"
textcolor = "#E4F4F5"
titletextcolor = "#5C87CB"


# Updates Frequency To Active Frequency / Amplitude
def updatefrequency1():
    global sinewave1
    global activeamplitude1
    global activefrequency1
    global sweeprate1
    global prevfreq1
    global freqsweepistrue1
    global hasstopped1
    if activeamplitude1 == 0:
        decibles = -100
    else:
        decibles = 10 * np.log2(activeamplitude1 / 100)
    if sweepfreq1.get():
        if not freqsweepistrue1 or hasstopped1:
            sinewave1.stop()
            pitch1 = 12 * np.log2(prevfreq1 / 440) + 9
            sinewave1 = SineWave(
                pitch=pitch1,
                pitch_per_second=sweeprate1,
                decibels_per_second=100000000,
                decibels=decibles,
            )
            sinewave1.play()
            freqsweepistrue1 = True
            hasstopped1 = False
        sinewave1.set_frequency(activefrequency1)
        sinewave1.set_volume(decibles)
    else:
        if freqsweepistrue1 or hasstopped1:
            sinewave1.stop()
            sinewave1 = SineWave(
                pitch=1,
                pitch_per_second=fastsweeprate1,
                decibels_per_second=100000000,
                decibels=decibles,
            )
            hasstopped1 = False
            sinewave1.play()
            freqsweepistrue1 = False
        sinewave1.set_frequency(activefrequency1)
        sinewave1.set_volume(decibles)

    dispfreqlabel1.config(text="Frequency: " + str(round(activefrequency1, 5)) + " Hz")
    dispamplabel1.config(text="Amplitude: " + str(round(activeamplitude1, 3)) + "%")
    prevfreq1 = activefrequency1


# Updates Frequency To Active Frequency / Amplitude
def updatefrequency2():
    global sinewave2
    global activeamplitude2
    global activefrequency2
    global sweeprate2
    global prevfreq2
    global freqsweepistrue2
    global hasstopped2
    if activeamplitude2 == 0:
        decibles = -100
    else:
        decibles = 10 * np.log2(activeamplitude2 / 100)
    if sweepfreq2.get():
        if not freqsweepistrue2 or hasstopped2:
            sinewave2.stop()
            pitch2 = 12 * np.log2(prevfreq2 / 440) + 9
            sinewave2 = SineWave(
                pitch=pitch2,
                pitch_per_second=sweeprate2,
                decibels_per_second=100000000,
                decibels=decibles,
            )
            sinewave2.play()
            freqsweepistrue2 = True
            hasstopped2 = False
        sinewave2.set_frequency(activefrequency1)
        sinewave2.set_volume(decibles)
    else:
        if freqsweepistrue2 or hasstopped2:
            sinewave2.stop()
            sinewave2 = SineWave(
                pitch=1,
                pitch_per_second=fastsweeprate2,
                decibels_per_second=100000000,
                decibels=decibles,
            )
            sinewave2.play()
            freqsweepistrue2 = False
            hasstopped2 = False
        sinewave2.set_frequency(activefrequency2)
        sinewave2.set_volume(decibles)

    dispfreqlabel2.config(text="Frequency: " + str(round(activefrequency2, 5)) + " Hz")
    dispamplabel2.config(text="Amplitude: " + str(round(activeamplitude2, 3)) + "%")
    prevfreq2 = activefrequency2


# Stops All Frequencies, Deselects Buttons, Resets Variables
def stopall():
    global activefrequency1
    global activefrequency2
    global activeamplitude1
    global activeamplitude2
    global customfrequency
    global customamplitude
    global customfrequency2
    global customamplitude2
    global sweepfreq1
    global sweepfreq2
    global freqsweepistrue1
    global freqsweepistrue2
    global hasstopped1
    global hasstopped2
    activefrequency1 = 0
    activefrequency2 = 0
    activeamplitude1 = 0
    activeamplitude2 = 0
    sinewave1.set_volume(-100)
    sinewave2.set_volume(-100)
    sinewave1.set_frequency(0)
    sinewave2.set_frequency(0)
    dispfreqlabel2.config(text="Frequency: " + str(round(activefrequency2, 5)) + " Hz")
    dispamplabel2.config(text="Amplitude: " + str(round(activeamplitude2, 3)) + "%")
    dispfreqlabel1.config(text="Frequency: " + str(round(activefrequency1, 5)) + " Hz")
    dispamplabel1.config(text="Amplitude: " + str(round(activeamplitude1, 3)) + "%")
    sweepfreq1.set(False)
    sweepfreq2.set(False)
    freqsweepistrue1 = True
    freqsweepistrue2 = True
    hasstopped1 = True
    hasstopped2 = True
    responsetosubmitlabel.config(text="")
    responsetosubmitlabel2.config(text="")
    DeselectButton.invoke()
    DeselectButton2.invoke()


def togglesweeprate1():
    global sweepfreq1
    global sweeprate1
    if sweepfreq1.get():
        sweeprate1 = slowsweeprate1
    else:
        sweeprate1 = fastsweeprate1
        updatefrequency1()


def togglesweeprate2():
    global sweepfreq2
    global sweeprate2
    if sweepfreq2.get():
        sweeprate2 = slowsweeprate2
    else:
        sweeprate2 = fastsweeprate2
        updatefrequency2()


# Applies Custom Frequency Information
def applycustom1():
    global customfrequency
    global customamplitude
    global activeamplitude1
    global activefrequency1
    private1 = DoubleVar()
    private2 = DoubleVar()
    responsetosubmitlabel.config(
        text="", background=backgroundcolor, foreground=textcolor
    )
    responsetosubmitlabel2.config(text="")
    validentry = BooleanVar(value=True)
    try:
        private1.set(customfrequency.get())
        private2.set(customamplitude.get())
    except Exception:
        validentry.set(value=False)
        responsetosubmitlabel.config(
            text="Invalid Entry!", background="Yellow", foreground="Black"
        )
        print("SET FREQ1 STRING ERROR")
        return

    if private1.get() < 0:
        responsetosubmitlabel.config(text="Frequency Too Low!")
        validentry.set(value=False)

    if private1.get() > 20000:
        responsetosubmitlabel.config(text="Frequency Too High!")
        validentry.set(value=False)

    if private2.get() < 0:
        responsetosubmitlabel2.config(text="Amplitude Too Low!")
        validentry.set(value=False)

    if private2.get() > 100:
        responsetosubmitlabel2.config(text="Amplitude Too High!")
        validentry.set(value=False)

    if validentry.get():
        activefrequency1 = float(private1.get())
        activeamplitude1 = float(private2.get())
        responsetosubmitlabel.config(text="Frequency Applied!")
        updatefrequency1()


# Applies Custom Frequency Information
def applycustom2():
    global customfrequency2
    global customamplitude2
    global activeamplitude2
    global activefrequency2
    private1 = DoubleVar()
    private2 = DoubleVar()
    responsetosubmitlabel3.config(
        text="", background=backgroundcolor, foreground=textcolor
    )
    responsetosubmitlabel4.config(text="")
    validentry = BooleanVar(value=True)
    try:
        private1.set(customfrequency2.get())
        private2.set(customamplitude2.get())
    except Exception:
        validentry.set(value=False)
        responsetosubmitlabel3.config(
            text="Invalid Entry!", background="Yellow", foreground="Black"
        )
        print("SET FREQ2 STRING ERROR")
        return
    if private1.get() < 0:
        responsetosubmitlabel3.config(text="Frequency Too Low!")
        validentry.set(value=False)

    if private1.get() > 20000:
        responsetosubmitlabel3.config(text="Frequency Too High!")
        validentry.set(value=False)

    if private2.get() < 0:
        responsetosubmitlabel4.config(text="Amplitude Too Low!")
        validentry.set(value=False)

    if private2.get() > 100:
        responsetosubmitlabel4.config(text="Amplitude Too High!")
        validentry.set(value=False)

    if validentry.get():
        activefrequency2 = float(private1.get())
        activeamplitude2 = float(private2.get())
        responsetosubmitlabel3.config(text="Frequency Applied!")
        updatefrequency2()


# Sets Active Frequency / Amplitude to Radiobutton Selection
def radiochangefreq1():
    global setting1amp
    global setting1freq
    global setting2amp
    global setting2freq
    global setting3amp
    global setting3freq
    global setting4amp
    global setting4freq
    global setting5amp
    global setting5freq
    global activeamplitude1
    global activefrequency1
    if str(selectionnumber.get()) == "1":
        activeamplitude1 = setting1amp
        activefrequency1 = setting1freq
    if str(selectionnumber.get()) == "2":
        activeamplitude1 = setting2amp
        activefrequency1 = setting2freq
    if str(selectionnumber.get()) == "3":
        activeamplitude1 = setting3amp
        activefrequency1 = setting3freq
    if str(selectionnumber.get()) == "4":
        activeamplitude1 = setting4amp
        activefrequency1 = setting4freq
    if str(selectionnumber.get()) == "5":
        activeamplitude1 = setting5amp
        activefrequency1 = setting5freq
    updatefrequency1()


# Sets Active Frequency / Amplitude to Radiobutton Selection
def radiochangefreq2():
    global setting1amp2
    global setting1freq2
    global setting2amp2
    global setting2freq2
    global setting3amp2
    global setting3freq2
    global setting4amp2
    global setting4freq2
    global setting5amp2
    global setting5freq2
    global activeamplitude2
    global activefrequency2
    if str(selectionnumber2.get()) == "1":
        activeamplitude2 = setting1amp2
        activefrequency2 = setting1freq2
    if str(selectionnumber2.get()) == "2":
        activeamplitude2 = setting2amp2
        activefrequency2 = setting2freq2
    if str(selectionnumber2.get()) == "3":
        activeamplitude2 = setting3amp2
        activefrequency2 = setting3freq2
    if str(selectionnumber2.get()) == "4":
        activeamplitude2 = setting4amp2
        activefrequency2 = setting4freq2
    if str(selectionnumber2.get()) == "5":
        activeamplitude2 = setting5amp2
        activefrequency2 = setting5freq2
    updatefrequency2()


def slidermenu():
    global sliderhasrun
    global slidermenuwindow
    responsetoslidermenu.config(
        text="", background=backgroundcolor, foreground=textcolor
    )
    if not sliderhasrun:
        createslidermenu()
        sliderhasrun = True
        return
    if hasattr(slidermenuwindow, "winfo_exists") and slidermenuwindow.winfo_exists():
        responsetoslidermenu.config(
            text="Window Already Open!", background="Yellow", foreground="Black"
        )
        return
    else:
        createslidermenu()


def createslidermenu():
    global slidermenuwindow
    global activefreqlabel1
    global activefreqlabel2
    slidermenuwindow = tk.Toplevel(root)
    slidermenuwindow.title("Frequency Sliders")
    slidermenuwindow.geometry("800x550")
    slidermenuwindow.configure(background=backgroundcolor)
    slidermenuwindow.resizable(False, False)
    slidermenuwindow.iconbitmap("ICERootLogo.ico")

    px80frameslider = Frame(
        slidermenuwindow, width=80, height=80, background=backgroundcolor
    )

    labelfreq1 = Label(
        slidermenuwindow,
        text="Frequency 1",
        font=("font", titlefontsize),
        background=backgroundcolor,
        fg=titletextcolor,
    )
    labelfreq2 = Label(
        slidermenuwindow,
        text="Frequency 2",
        font=("font", titlefontsize),
        background=backgroundcolor,
        fg=titletextcolor,
    )
    activefreqlabel1 = Label(
        slidermenuwindow,
        font=("font", smallfontsize),
        background=backgroundcolor,
        fg=textcolor,
    )
    activefreqlabel2 = Label(
        slidermenuwindow,
        font=("font", smallfontsize),
        background=backgroundcolor,
        fg=textcolor,
    )
    amplitudebutton1 = Button(
        slidermenuwindow,
        command=setamplitude1topreset,
        text="Set Frequency 1 Amplitude to " + str(freq1buttonpreset) + "%",
        font=("font", tinyfontsize),
        background=backgroundcolor,
        fg=textcolor,
    )
    amplitudebutton2 = Button(
        slidermenuwindow,
        command=setamplitude2topreset,
        text="Set Frequency 2 Amplitude to " + str(freq2buttonpreset) + "%",
        font=("font", tinyfontsize),
        background=backgroundcolor,
        fg=textcolor,
    )
    slider1 = Scale(
        slidermenuwindow,
        variable=sliderfrequency1,
        from_=freq1sliderlow,
        to=freq1sliderhigh,
        orient=HORIZONTAL,
        length=750,
        resolution=scaleresolution,
        command=sliderupdate1,
        background=backgroundcolor,
        fg=textcolor,
    )
    slider2 = Scale(
        slidermenuwindow,
        variable=sliderfrequency2,
        from_=freq2sliderlow,
        to=freq2sliderhigh,
        orient=HORIZONTAL,
        length=750,
        resolution=scaleresolution,
        command=sliderupdate2,
        background=backgroundcolor,
        fg=textcolor,
    )

    labelfreq1.grid(column=5, row=0, pady=5)
    slider1.grid(column=0, columnspan=10, row=2, padx=25, pady=10)
    activefreqlabel1.grid(column=5, row=3, pady=5)
    amplitudebutton1.grid(column=5, row=4, pady=5)
    px80frameslider.grid(column=5, row=5)
    labelfreq2.grid(column=5, row=6, pady=5)
    slider2.grid(column=0, columnspan=10, row=8, padx=25, pady=10)
    activefreqlabel2.grid(column=5, row=9, pady=5)
    amplitudebutton2.grid(column=5, row=10, pady=5)
    activefreqlabel1.config(
        text="Frequency: " + str(round(activefrequency1, 5)) + " Hz"
    )
    activefreqlabel2.config(
        text="Frequency: " + str(round(activefrequency2, 5)) + " Hz"
    )


def sliderupdate1(frequency):
    global activefrequency1
    global sinewave1
    global sweepfreq1
    global activefreqlabel1
    global hasstopped1
    global selectionnumber
    if selectionnumber != 0:
        DeselectButton.invoke()
    if sweepfreq1.get() or hasstopped1:
        sweepfreq1.set(False)
        updatefrequency1()
        hasstopped1 = False
    activefrequency1 = sliderfrequency1.get()
    sinewave1.set_frequency(activefrequency1)
    dispfreq1 = "Frequency: " + str(round(activefrequency1, 5)) + " Hz"
    dispfreqlabel1.config(text=dispfreq1)
    activefreqlabel1.config(text=dispfreq1)


def sliderupdate2(frequency):
    global activefrequency2
    global sinewave2
    global sweepfreq2
    global activefreqlabel2
    global hasstopped2
    global selectionnumber2
    if selectionnumber2 != 0:
        DeselectButton2.invoke()
    if sweepfreq2.get() or hasstopped2:
        sweepfreq2.set(False)
        updatefrequency2()
        hasstopped2 = False
    activefrequency2 = sliderfrequency2.get()
    sinewave2.set_frequency(activefrequency2)
    dispfreq2 = "Frequency: " + str(round(activefrequency2, 5)) + " Hz"
    dispfreqlabel2.config(text=dispfreq2)
    activefreqlabel2.config(text=dispfreq2)


def setamplitude1topreset():
    global activeamplitude1
    global sinewave1
    activeamplitude1 = freq1buttonpreset
    if activeamplitude1 == 0:
        decibles = -100
    else:
        decibles = 10 * np.log2(activeamplitude1 / 100)
    sinewave1.set_volume(decibles)
    dispamplabel1.config(text="Amplitude: " + str(round(activeamplitude1, 3)) + "%")


def setamplitude2topreset():
    global activeamplitude2
    global sinewave2
    activeamplitude2 = freq2buttonpreset
    if activeamplitude2 == 0:
        decibles = -100
    else:
        decibles = 10 * np.log2(activeamplitude2 / 100)
    sinewave2.set_volume(decibles)
    dispamplabel2.config(text="Amplitude: " + str(round(activeamplitude2, 3)) + "%")


# Create Root GUI
root = Tk()
root.title("Frequency Generator " + version)
root.geometry("1220x800")
root.configure(background=backgroundcolor)
root.resizable(False, False)
root.iconbitmap("ICERootLogo.ico")

sliderhasrun = False

# Create SineWave Objects
sinewave1 = SineWave()
sinewave2 = SineWave()

# Define Custom Frequencies
customfrequency = DoubleVar()
customamplitude = DoubleVar()
customfrequency2 = DoubleVar()
customamplitude2 = DoubleVar()
sliderfrequency1 = DoubleVar()
sliderfrequency2 = DoubleVar()
sweepfreq1 = BooleanVar(value=False)
sweepfreq2 = BooleanVar(value=False)
freqsweepistrue1 = True
freqsweepistrue2 = True
sweeprate1 = fastsweeprate1
sweeprate2 = fastsweeprate2

hasstopped1 = False
hasstopped2 = False

# Create Logo Block
image = Image.open("ICElogo.png")
newsize = (425, 334)
resizedimage = image.resize(newsize)
logo = ImageTk.PhotoImage(resizedimage)
logolabel = Label(root, image=logo, border=0)
# Place Logo Block
logolabel.grid(column=5, row=2, rowspan=8)

# Create Selection Buttons
presets = Radiobutton(root)
selectionnumber = IntVar()
R11 = Radiobutton(
    root,
    text=setting1name,
    variable=selectionnumber,
    value=1,
    command=radiochangefreq1,
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
    selectcolor=backgroundcolor,
)
R21 = Radiobutton(
    root,
    text=setting2name,
    variable=selectionnumber,
    value=2,
    command=radiochangefreq1,
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
    selectcolor=backgroundcolor,
)
R31 = Radiobutton(
    root,
    text=setting3name,
    variable=selectionnumber,
    value=3,
    command=radiochangefreq1,
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
    selectcolor=backgroundcolor,
)
R41 = Radiobutton(
    root,
    text=setting4name,
    variable=selectionnumber,
    value=4,
    command=radiochangefreq1,
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
    selectcolor=backgroundcolor,
)
R51 = Radiobutton(
    root,
    text=setting5name,
    variable=selectionnumber,
    value=5,
    command=radiochangefreq1,
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
    selectcolor=backgroundcolor,
)
DeselectButton = Radiobutton(
    root,
    variable=selectionnumber,
    value=0,
)

presets2 = Radiobutton(root)
selectionnumber2 = IntVar()
R12 = Radiobutton(
    root,
    text=setting1name2,
    variable=selectionnumber2,
    value=1,
    command=radiochangefreq2,
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
    selectcolor=backgroundcolor,
)
R22 = Radiobutton(
    root,
    text=setting2name2,
    variable=selectionnumber2,
    value=2,
    command=radiochangefreq2,
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
    selectcolor=backgroundcolor,
)
R32 = Radiobutton(
    root,
    text=setting3name2,
    variable=selectionnumber2,
    value=3,
    command=radiochangefreq2,
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
    selectcolor=backgroundcolor,
)
R42 = Radiobutton(
    root,
    text=setting4name2,
    variable=selectionnumber2,
    value=4,
    command=radiochangefreq2,
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
    selectcolor=backgroundcolor,
)
R52 = Radiobutton(
    root,
    text=setting5name2,
    variable=selectionnumber2,
    value=5,
    command=radiochangefreq2,
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
    selectcolor=backgroundcolor,
)
DeselectButton2 = Radiobutton(
    root,
    variable=selectionnumber2,
    value=0,
)


# Place Selection Buttons
R11.grid(column=0, row=2)
R21.grid(column=0, row=3)
R31.grid(column=0, row=4)
R41.grid(column=0, row=5)
R51.grid(column=0, row=6)
R12.grid(column=10, row=2)
R22.grid(column=10, row=3)
R32.grid(column=10, row=4)
R42.grid(column=10, row=5)
R52.grid(column=10, row=6)

# Create Labels / Entries
labeltitle = Label(
    root,
    text="Frequency Generator",
    font=("font", titlefontsize),
    background=backgroundcolor,
    fg=titletextcolor,
)
labeltitle.config(anchor=CENTER)
freq1label = Label(
    root,
    text="Set Frequency 1",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=titletextcolor,
)
freq2label = Label(
    root,
    text="Set Frequency 2",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=titletextcolor,
)
dispfreqlabel1 = Label(
    root, font=("font", smallfontsize), background=backgroundcolor, fg=textcolor
)
dispamplabel1 = Label(
    root, font=("font", smallfontsize), background=backgroundcolor, fg=textcolor
)
dispfreqlabel2 = Label(
    root, font=("font", smallfontsize), background=backgroundcolor, fg=textcolor
)
dispamplabel2 = Label(
    root, font=("font", smallfontsize), background=backgroundcolor, fg=textcolor
)
customtitlelabel = Label(
    root,
    text="Set a Custom Frequency",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
)
customtitlelabel2 = Label(
    root,
    text="Set a Custom Frequency",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
)
customfreqlabel = Label(
    root,
    text="Hz",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
)
customfreqlabel2 = Label(
    root,
    text="Hz",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
)
customamplabel = Label(
    root,
    text="%",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
)
customamplabel2 = Label(
    root,
    text="%",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
)
cfrequencyentry = Entry(
    root,
    textvariable=customfrequency,
    font=("font", smallfontsize),
    background=backgroundcolor,
    insertbackground=textcolor,
    justify="right",
    fg=textcolor,
    borderwidth=0,
    highlightcolor=textcolor,
    highlightthickness=2,
)
cfrequencyentry2 = Entry(
    root,
    textvariable=customfrequency2,
    font=("font", smallfontsize),
    background=backgroundcolor,
    insertbackground=textcolor,
    justify="right",
    fg=textcolor,
    borderwidth=0,
    highlightcolor=textcolor,
    highlightthickness=2,
)
camplitudeentry = Entry(
    root,
    textvariable=customamplitude,
    font=("font", smallfontsize),
    background=backgroundcolor,
    insertbackground=textcolor,
    justify="right",
    fg=textcolor,
    borderwidth=0,
    highlightcolor=textcolor,
    highlightthickness=2,
)
camplitudeentry2 = Entry(
    root,
    textvariable=customamplitude2,
    font=("font", smallfontsize),
    background=backgroundcolor,
    insertbackground=textcolor,
    justify="right",
    fg=textcolor,
    borderwidth=0,
    highlightcolor=textcolor,
    highlightthickness=2,
)
submitbutton = Button(
    root,
    command=applycustom1,
    text="Apply Custom Frequency",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
)
submitbutton2 = Button(
    root,
    command=applycustom2,
    text="Apply Custom Frequency",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
)
stopallbutton = Button(
    root,
    text="Stop Both Frequencies",
    font=("font", smallfontsize),
    command=stopall,
    background=backgroundcolor,
    fg=textcolor,
)
sweepcheck1 = Checkbutton(
    root,
    text="Sweep",
    variable=sweepfreq1,
    command=togglesweeprate1,
    foreground=textcolor,
    background=backgroundcolor,
    selectcolor=backgroundcolor,
    font=("font", tinyfontsize),
)
sweepcheck2 = Checkbutton(
    root,
    text="Sweep",
    variable=sweepfreq2,
    command=togglesweeprate2,
    foreground=textcolor,
    background=backgroundcolor,
    selectcolor=backgroundcolor,
    font=("font", tinyfontsize),
)

slidermenubutton = Button(
    command=slidermenu,
    text="Open Slider Menu",
    font=("font", smallfontsize),
    background=backgroundcolor,
    fg=textcolor,
)

responsetosubmitlabel = Label(
    root, font=("font", smallfontsize), background=backgroundcolor, fg=textcolor
)
responsetosubmitlabel2 = Label(
    root, font=("font", smallfontsize), background=backgroundcolor, fg=textcolor
)
responsetosubmitlabel3 = Label(
    root, font=("font", smallfontsize), background=backgroundcolor, fg=textcolor
)
responsetosubmitlabel4 = Label(
    root, font=("font", smallfontsize), background=backgroundcolor, fg=textcolor
)
responsetoslidermenu = Label(
    root, font=("font", smallfontsize), background=backgroundcolor, fg=textcolor
)

# Create Spacing Elements
px40frame = Frame(root, width=40, height=40, background=backgroundcolor)

# Place Above Label, Entries, Spacing Elements
labeltitle.grid(column=5, row=0)
freq1label.grid(column=0, row=1)
freq2label.grid(column=10, row=1)
dispfreqlabel1.grid(column=0, row=8)
dispamplabel1.grid(column=0, row=9)
dispfreqlabel2.grid(column=10, row=8)
dispamplabel2.grid(column=10, row=9)
stopallbutton.grid(column=5, row=11)
customtitlelabel.grid(column=0, row=11)
px40frame.grid(column=10, row=10)
customtitlelabel2.grid(column=10, row=11)
cfrequencyentry.grid(column=0, row=13)
cfrequencyentry2.grid(column=10, row=13)
customfreqlabel.grid(column=1, row=13)
customfreqlabel2.grid(column=11, row=13)
customamplabel.grid(column=0, row=15)
customamplabel2.grid(column=10, row=15)
camplitudeentry.grid(column=0, row=16)
camplitudeentry2.grid(column=10, row=16)
customamplabel.grid(column=1, row=16)
customamplabel2.grid(column=11, row=16)
sweepcheck1.grid(column=0, row=18)
sweepcheck2.grid(column=10, row=18)
submitbutton.grid(column=0, row=20)
submitbutton2.grid(column=10, row=20)
responsetosubmitlabel.grid(column=0, row=22, pady=3)
responsetosubmitlabel2.grid(column=0, row=23,pady=3)
responsetosubmitlabel3.grid(column=10, row=22,pady=3)
responsetosubmitlabel4.grid(column=10, row=23,pady=3)
slidermenubutton.grid(column=5, row=20)
responsetoslidermenu.grid(column=5, row=22)

warnings.filterwarnings("ignore", category=RuntimeWarning)

# Start Initial Frequencies
updatefrequency1()
updatefrequency2()

# Begin GUI Loop
root.mainloop()
