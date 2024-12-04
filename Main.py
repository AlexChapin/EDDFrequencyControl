from tkinter import *
from PIL import ImageTk, Image
from pysinewave import SineWave
import time
import numpy as np
# Default Frequency On Startup
startupfreq1 = 450
startupamp1 = 0.5

startupfreq2 = 200
startupamp2 = 0.5

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

#SineWave Init Configs









setting1name = str(setting1freq) + "Hz / " + str(setting1amp * 100) + "% Amplitude"
setting2name = str(setting2freq) + "Hz / " + str(setting2amp * 100) + "% Amplitude"
setting3name = str(setting3freq) + "Hz / " + str(setting3amp * 100) + "% Amplitude"
setting4name = str(setting4freq) + "Hz / " + str(setting4amp * 100) + "% Amplitude"
setting5name = str(setting5freq) + "Hz / " + str(setting5amp * 100) + "% Amplitude"

activefrequency1 = startupfreq1
activeamplitude1 = startupamp1
activefrequency2 = startupfreq2
activeamplitude2 = startupamp2


# GUI Global Settings
backgroundcolor = "#0084bd"
textcolor = "black"

interrupt = False


def updatefrequency1():
    global sinewave1
    global activeamplitude1
    global activefrequency1
    sinewave1.stop()
    time.sleep(.03)
    sinewave1.set_frequency(activefrequency1)
    sinewave1.set_volume(10 * np.log2( activeamplitude1))
    time.sleep(.03)
    sinewave1.play()

def updatefrequency2():
    global sinewave2
    global activeamplitude2
    global activefrequency2
    sinewave2.stop()
    time.sleep(.03)
    sinewave2.set_frequency(activefrequency2)
    sinewave2.set_volume(10 * np.log2( activeamplitude2))
    time.sleep(.03)
    sinewave2.play()

def applycustom():
    print("custom frequency applied")


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
    active = "Active Selection: "
    if str(selectionnumber.get()) == "1":
        selection = setting1name
        activeamplitude1 = setting1amp
        activefrequency1 = setting1freq
    if str(selectionnumber.get()) == "2":
        selection = setting2name
        activeamplitude1 = setting2amp
        activefrequency1 = setting2freq
    if str(selectionnumber.get()) == "3":
        selection = setting3name
        activeamplitude1 = setting3amp
        activefrequency1 = setting3freq
    if str(selectionnumber.get()) == "4":
        selection = setting4name
        activeamplitude1 = setting4amp
        activefrequency1 = setting4freq
    if str(selectionnumber.get()) == "5":
        selection = setting5name
        activeamplitude1 = setting5amp
        activefrequency1 = setting5freq
    activelabel.config(text=active + selection)
    updatefrequency1()

def radiochangefreq2():
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
    active = "Active Selection: "
    if str(selectionnumber.get()) == "1":
            selection = setting1name
            activeamplitude1 = setting1amp
            activefrequency1 = setting1freq
    if str(selectionnumber.get()) == "2":
        selection = setting2name
        activeamplitude1 = setting2amp
        activefrequency1 = setting2freq
    if str(selectionnumber.get()) == "3":
        selection = setting3name
        activeamplitude1 = setting3amp
        activefrequency1 = setting3freq
    if str(selectionnumber.get()) == "4":
        selection = setting4name
        activeamplitude1 = setting4amp
        activefrequency1 = setting4freq
    if str(selectionnumber.get()) == "5":
        selection = setting5name
        activeamplitude1 = setting5amp
        activefrequency1 = setting5freq
    activelabel.config(text=active + selection)
    updatefrequency2()

#Create Root GUI
root = Tk()
root.title("Frequency Generator v1.0.0a")
root.geometry("1280x810")
root.configure(background="#0084bd")
root.resizable(False, False)

#Create SineWave Option
sinewave1 = SineWave(pitch=1, pitch_per_second=1000000000, decibels_per_second=1)
sinewave2 = SineWave(pitch=1, pitch_per_second=1000000000, decibels_per_second=1)

#Create Title Label
labeltitle = Label(
    root,
    text="Frequency Generator",
    font=("Century", 35),
    background=backgroundcolor,
    fg=textcolor,
)
labeltitle.config(anchor=CENTER)
labeltitle.grid(column=10,row=0)


# logo = ImageTk.PhotoImage(Image.open(""))

freq1label = Label(text="Set Frequency 1",font=("Century", 20), background=backgroundcolor, fg=textcolor)
freq1label.grid(column=0,row=1)
#Create Active Label
activelabel = Label(
    root, font=("Century", 20), background=backgroundcolor, fg=textcolor
)
#activelabel.pack(anchor=W)


#Create Selection Buttons
presets = Radiobutton(root)
selectionnumber = IntVar()
R1 = Radiobutton(
    root,
    text=setting1name,
    variable=selectionnumber,
    value=1,
    command= radiochangefreq1,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R1.grid(column=0,row=2,ipadx=5)
R2 = Radiobutton(
    root,
    text=setting2name,
    variable=selectionnumber,
    value=2,
    command= radiochangefreq1,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R2.grid(column=0,row=3)
R3 = Radiobutton(
    root,
    text=setting3name,
    variable=selectionnumber,
    value=3,
    command= radiochangefreq1,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R3.grid(column=0,row=4)
R4 = Radiobutton(
    root,
    text=setting4name,
    variable=selectionnumber,
    value=4,
    command= radiochangefreq1,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R4.grid(column=0,row=5)
R5 = Radiobutton(
    root,
    text=setting5name,
    variable=selectionnumber,
    value=5,
    command= radiochangefreq1,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R5.grid(column=0,row=6)

presets2 = Radiobutton(root)
selectionnumber2 = IntVar()
R1 = Radiobutton(
    root,
    text=setting1name,
    variable=selectionnumber2,
    value=1,
    command=radiochangefreq2,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
R1.grid(column=11,row=2)
R2 = Radiobutton(
    root,
    text=setting2name,
    variable=selectionnumber2,
    value=2,
    command=radiochangefreq2,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
#R2.pack(anchor=N)
R3 = Radiobutton(
    root,
    text=setting3name,
    variable=selectionnumber2,
    value=3,
    command=radiochangefreq2,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
#R3.pack(anchor=E)
R4 = Radiobutton(
    root,
    text=setting4name,
    variable=selectionnumber2,
    value=4,
    command=radiochangefreq2,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
#R4.pack(anchor=E)
R5 = Radiobutton(
    root,
    text=setting5name,
    variable=selectionnumber2,
    value=5,
    command=radiochangefreq2,
    font=("Century", 20),
    background=backgroundcolor,
    fg=textcolor,
)
#R5.pack(anchor=E)


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
#customtitlelabel.pack(anchor=S)
#customfreqlabel.pack(anchor=S)
#cfrequencyentry.pack(anchor=S)
#customamplabel.pack(anchor=S)
#camplitudeentry.pack(anchor=S)
responsetosubmitlabel = Label(
    root, font=("Century", 20), background=backgroundcolor, fg=textcolor
)

#submitbutton.pack(anchor=S)

root.mainloop()
