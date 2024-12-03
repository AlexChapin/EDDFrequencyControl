from tkinter import *
from PIL import ImageTk, Image
import time
import numpy as np
import sounddevice as sd

# Default Frequency On Startup
startupfreq = 0
startupamp = 0


# Frequency Settings
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

setting1name = str(setting1freq) + "Hz / " + str(setting1amp * 100) + "% Amplitude"
setting2name = str(setting2freq) + "Hz / " + str(setting2amp * 100) + "% Amplitude"
setting3name = str(setting3freq) + "Hz / " + str(setting3amp * 100) + "% Amplitude"
setting4name = str(setting4freq) + "Hz / " + str(setting4amp * 100) + "% Amplitude"
setting5name = str(setting5freq) + "Hz / " + str(setting5amp * 100) + "% Amplitude"

activefrequency = startupfreq
activeamplitude = startupamp

# GUI Global Settings
backgroundcolor = "#0084bd"
textcolor = "black"

interrupt = False


def updatefrequency():
    t = np.linspace(0, 3, int(44100 * 1), False)
    waveform = np.sin(2 * np.pi * 200 * t)
    sd.default.samplerate = 44100
    sd.play(waveform, blocking=False)
    # sd.play(, blocking=False)


def applycustom():
    print("custom frequency applied")
    sd.stop()


def updatelable():
    active = "Active Selection: "
    if str(selectionnumber.get()) == "1":
        selection = setting1name
    if str(selectionnumber.get()) == "2":
        selection = setting2name
    if str(selectionnumber.get()) == "3":
        selection = setting3name
    if str(selectionnumber.get()) == "4":
        selection = setting4name
    if str(selectionnumber.get()) == "5":
        selection = setting5name
    activelabel.config(text=active + selection)
    updatefrequency()


root = Tk()
root.title("Frequency Generator v1.0.0a")
root.geometry("800x800")
root.configure(background="#0084bd")
root.resizable(False, False)

labeltitle = Label(
    root,
    text="Frequency Generator",
    font=("Century", 35),
    background=backgroundcolor,
    fg=textcolor,
)
labeltitle.config(anchor=CENTER)
labeltitle.pack()


# logo = ImageTk.PhotoImage(Image.open(""))

presets = Radiobutton(root)

activelabel = Label(
    root, font=("Century", 20), background=backgroundcolor, fg=textcolor
)
activelabel.pack(anchor=W)

selectionnumber = IntVar()
R1 = Radiobutton(
    root,
    text=setting1name,
    variable=selectionnumber,
    value=1,
    command=updatelable,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R1.pack(anchor=W)
R2 = Radiobutton(
    root,
    text=setting2name,
    variable=selectionnumber,
    value=2,
    command=updatelable,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R2.pack(anchor=W)
R3 = Radiobutton(
    root,
    text=setting3name,
    variable=selectionnumber,
    value=3,
    command=updatelable,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R3.pack(anchor=W)
R4 = Radiobutton(
    root,
    text=setting4name,
    variable=selectionnumber,
    value=4,
    command=updatelable,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R4.pack(anchor=W)
R5 = Radiobutton(
    root,
    text=setting5name,
    variable=selectionnumber,
    value=5,
    command=updatelable,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R5.pack(anchor=W)

customfrequency = Variable
customamplitude = Variable
customtitlelabel = Label(
    root,
    text="Set a Custom Frequency",
    font=("Century", 30),
    background=backgroundcolor,
    fg=textcolor,
)
customfreqlabel = Label(
    root,
    text="Frequency",
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
customamplabel = Label(
    root,
    text="Amplitude",
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
cfrequencyentry = Entry(
    root,
    textvariable=customfrequency,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
camplitudeentry = Entry(
    root,
    textvariable=customamplitude,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
submitbutton = Button(
    root,
    command=applycustom,
    text="Apply Custom Frequency",
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
customtitlelabel.pack(anchor=S)
customfreqlabel.pack(anchor=S)
cfrequencyentry.pack(anchor=S)
customamplabel.pack(anchor=S)
camplitudeentry.pack(anchor=S)
responsetosubmitlabel = Label(
    root, font=("Century", 20), background=backgroundcolor, fg=textcolor
)

submitbutton.pack(anchor=S)


root.mainloop()
