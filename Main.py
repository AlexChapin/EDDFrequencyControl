from tkinter import *
from PIL import ImageTk, Image
from pysinewave import SineWave
import numpy as np
import warnings
import time

# BE CAREFUL CHANGING THESE!!! 
# DON'T SET FREQUENCY TO < 1 or > 20000
# DON'T SET AMPLITUDE TO > 100
# Default Frequency On Startup
startupfreq1 = 0
startupamp1 = 0.5

startupfreq2 = 0
startupamp2 = 0.5

# Frequency 1 Settings
setting1freq = 100
setting1amp = 1

setting2freq = 200
setting2amp = 1

setting3freq = 300
setting3amp = 1

setting4freq = 400
setting4amp = 1

setting5freq = 500
setting5amp = 1

# Frequency 2 Settings
setting1freq2 = 100
setting1amp2 = 1

setting2freq2 = 200
setting2amp2 = 1

setting3freq2 = 300
setting3amp2 = 1

setting4freq2 = 400
setting4amp2 = 1

setting5freq2 = 500
setting5amp2 = 1

# Version Number:
version = "v1.0.1"

# Establish Setting Names
setting1name = str(setting1freq) + " Hz / " + str(setting1amp * 100) + "% Amplitude"
setting2name = str(setting2freq) + " Hz / " + str(setting2amp * 100) + "% Amplitude"
setting3name = str(setting3freq) + " Hz / " + str(setting3amp * 100) + "% Amplitude"
setting4name = str(setting4freq) + " Hz / " + str(setting4amp * 100) + "% Amplitude"
setting5name = str(setting5freq) + " Hz / " + str(setting5amp * 100) + "% Amplitude"

setting1name2 = str(setting1freq2) + " Hz / " + str(setting1amp2 * 100) + "% Amplitude"
setting2name2 = str(setting2freq2) + " Hz / " + str(setting2amp2 * 100) + "% Amplitude"
setting3name2 = str(setting3freq2) + " Hz / " + str(setting3amp2 * 100) + "% Amplitude"
setting4name2 = str(setting4freq2) + " Hz / " + str(setting4amp2 * 100) + "% Amplitude"
setting5name2 = str(setting5freq2) + " Hz / " + str(setting5amp2 * 100) + "% Amplitude"

# Set Initial Frequencies
activefrequency1 = startupfreq1
activeamplitude1 = startupamp1
activefrequency2 = startupfreq2
activeamplitude2 = startupamp2


# GUI Global Settings
font = "Century"
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
    sinewave1.stop()
    if activeamplitude1 == 0:
        decibles = -100
    else:
        decibles = 10 * np.log2(activeamplitude1)
    sinewave1 = SineWave(
        pitch=1,
        pitch_per_second=1000000000,
        decibels_per_second=1,
        decibels=decibles,
    )

    time.sleep(0.03)
    sinewave1.set_frequency(activefrequency1)
    time.sleep(0.03)
    sinewave1.play()
    dispfreqlabel1.config(text="Frequency: " + str(round(activefrequency1,5)) + " Hz")
    dispamplabel1.config(text="Amplitude: " + str(round(activeamplitude1 * 100,3)) + "%")


# Updates Frequency To Active Frequency / Amplitude
def updatefrequency2():
    global sinewave2
    global activeamplitude2
    global activefrequency2
    sinewave2.stop()
    if activeamplitude2 == 0:
        decibles = -100
    else:
        decibles = 10 * np.log2(activeamplitude2)
    sinewave2 = SineWave(
        pitch=1,
        pitch_per_second=1000000000,
        decibels_per_second=1,
        decibels=decibles,
    )

    time.sleep(0.03)
    sinewave2.set_frequency(activefrequency2)
    time.sleep(0.03)
    sinewave2.play()
    dispfreqlabel2.config(text="Frequency: " + str(round(activefrequency2,5)) + " Hz")
    dispamplabel2.config(text="Amplitude: " + str(round(activeamplitude2 * 100,3)) + "%")


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
    activefrequency1 = 0
    activefrequency2 = 0
    activeamplitude1 = 0
    activeamplitude2 = 0
    updatefrequency1()
    updatefrequency2()
    responsetosubmitlabel.config(text="")
    responsetosubmitlabel2.config(text="")
    R11.deselect()
    R21.deselect()
    R31.deselect()
    R41.deselect()
    R51.deselect()
    R12.deselect()
    R22.deselect()
    R32.deselect()
    R42.deselect()
    R52.deselect()


# Applies Custom Frequency Information
def applycustom1():
    global customfrequency
    global customamplitude
    global activeamplitude1
    global activefrequency1
    private1 = DoubleVar()
    private2 = DoubleVar()
    responsetosubmitlabel.config(text="", background=backgroundcolor, foreground=textcolor)
    responsetosubmitlabel2.config(text="")
    validentry = BooleanVar(value=True)
    try:
        private1.set(customfrequency.get())
        private2.set(customamplitude.get() / 100)
    except Exception:
        validentry.set(value=False)
        responsetosubmitlabel.config(text="Invalid Entry!", background="Yellow", foreground="Black")
        print("SET FREQ1 STRING ERROR")
        return

    if private1.get() < 1:
        responsetosubmitlabel.config(text="Frequency Too Low!")
        validentry.set(value=False)

    if private1.get() > 20000:
        responsetosubmitlabel.config(text="Frequency Too High!")
        validentry.set(value=False)

    if private2.get() < 0:
        responsetosubmitlabel2.config(text="Amplitude Too Low!")
        validentry.set(value=False)

    if private2.get() > 1:
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
    responsetosubmitlabel3.config(text="", background=backgroundcolor, foreground=textcolor)
    responsetosubmitlabel4.config(text="")
    validentry = BooleanVar(value=True)
    try:
        private1.set(customfrequency2.get())
        private2.set(customamplitude2.get() / 100)
    except Exception:
        validentry.set(value=False)
        responsetosubmitlabel3.config(text="Invalid Entry!", background="Yellow",foreground="Black")
        print("SET FREQ2 STRING ERROR")
        return
    if private1.get() < 1:
        responsetosubmitlabel3.config(text="Frequency Too Low!")
        validentry.set(value=False)

    if private1.get() > 20000:
        responsetosubmitlabel3.config(text="Frequency Too High!")
        validentry.set(value=False)

    if private2.get() < 0:
        responsetosubmitlabel4.config(text="Amplitude Too Low!")
        validentry.set(value=False)

    if private2.get() > 1:
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
    active = "Active Selection: "
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


# Create Root GUI
root = Tk()
root.title("Frequency Generator "+version)
root.geometry("1220x770")
root.configure(background=backgroundcolor)
root.resizable(False, False)

# Create SineWave Objects
sinewave1 = SineWave(
    pitch=1, pitch_per_second=1000000000, decibels_per_second=1, decibels=0
)
sinewave2 = SineWave(
    pitch=1, pitch_per_second=1000000000, decibels_per_second=1, decibels=0
)

# Define Custom Frequencies
customfrequency = DoubleVar()
customamplitude = DoubleVar()
customfrequency2 = DoubleVar()
customamplitude2 = DoubleVar()

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
    highlightthickness=2
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
    highlightthickness=2
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
    highlightthickness=2
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
    highlightthickness=2
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

# Create Spacing Elements
px40frame = Frame(root, width=40, height=40, background=backgroundcolor)
px10frame = Frame(root, width=10, height=10, background=backgroundcolor)
px5frame = Frame(root, width=5, height=5, background=backgroundcolor)

# Place Above Label, Entries, Spacing Elements
labeltitle.grid(column=5, row=0)
freq1label.grid(column=0, row=1)
freq2label.grid(column=10, row=1)
dispfreqlabel1.grid(column=0, row=8)
dispamplabel1.grid(column=0, row=9)
dispfreqlabel2.grid(column=10, row=8)
dispamplabel2.grid(column=10, row=9)
stopallbutton.grid(column=5, row=11)
px5frame.grid(column=5, row=10)
px40frame.grid(column=0, row=10)
customtitlelabel.grid(column=0, row=11)
px40frame.grid(column=10, row=10)
customtitlelabel2.grid(column=10, row=11)
px5frame.grid(column=0, row=12)
px5frame.grid(column=10, row=12)
cfrequencyentry.grid(column=0, row=13)
cfrequencyentry2.grid(column=10, row=13)
customfreqlabel.grid(column=1, row=13)
customfreqlabel2.grid(column=11, row=13)
px10frame.grid(column=0, row=14)
px10frame.grid(column=10, row=14)
customamplabel.grid(column=0, row=15)
customamplabel2.grid(column=10, row=15)
camplitudeentry.grid(column=0, row=16)
camplitudeentry2.grid(column=10, row=16)
customamplabel.grid(column=1, row=16)
customamplabel2.grid(column=11, row=16)
px10frame.grid(column=0, row=17)
px10frame.grid(column=10, row=17)
submitbutton.grid(column=0, row=18)
submitbutton2.grid(column=10, row=18)
px5frame.grid(column=0, row=19)
px5frame.grid(column=10, row=19)
responsetosubmitlabel.grid(column=0, row=20)
responsetosubmitlabel2.grid(column=0, row=21)
responsetosubmitlabel3.grid(column=10, row=20)
responsetosubmitlabel4.grid(column=10, row=21)

warnings.filterwarnings("ignore", category=RuntimeWarning)

# Start Initial Frequencies
updatefrequency1()
updatefrequency2()

# Begin GUI Loop
root.mainloop()
