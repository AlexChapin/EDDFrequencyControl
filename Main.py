from tkinter import *
from PIL import ImageTk, Image

def updatefrequency():
   print(0)


def updatelable():
   active="Active Selection: "
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
   activelabel.config(text = active + selection)
   updatefrequency()

#GUI Global Settings
backgroundcolor = "#0084bd"
textcolor = "black"


#Frequency Settings
setting1name = "100 Hz / 100% Amplitude (Sine)"
setting2name = "200 Hz / 100% Amplitude (Sine)"
setting3name = "300 Hz / 100% Amplitude (Sine)"
setting4name = "400 Hz / 100% Amplitude (Sine)"
setting5name = "500 Hz / 100% Amplitude (Sine)"


root = Tk()
root.title("Frequency Generator v1.0.0a")
root.geometry('800x800')
root.configure(background='#0084bd')
root.resizable(False, False)

label1 = Label(root, text="Frequency Generator", font=("Century", 35), background=backgroundcolor, fg=textcolor)
label1.config(anchor=CENTER)
label1.pack()



#logo = ImageTk.PhotoImage(Image.open(""))

presets = Radiobutton(root)

activelabel = Label(root,font=("Century", 20), background=backgroundcolor, fg=textcolor)
activelabel.pack(anchor = W)

selectionnumber = IntVar()
R1 = Radiobutton(root, text=setting1name, variable=selectionnumber, value=1, command=updatelable, font=("Century", 20), background=backgroundcolor, fg=textcolor)
R1.pack(anchor = W)
R2 = Radiobutton(root, text=setting2name, variable=selectionnumber, value=2, command=updatelable, font=("Century", 20), background=backgroundcolor, fg=textcolor)
R2.pack(anchor = W)
R3 = Radiobutton(root, text=setting3name, variable=selectionnumber, value=3, command=updatelable, font=("Century", 20), background=backgroundcolor, fg=textcolor)
R3.pack(anchor = W)
R4 = Radiobutton(root, text=setting4name, variable=selectionnumber, value=4, command=updatelable, font=("Century", 20), background=backgroundcolor, fg=textcolor)
R4.pack(anchor = W)
R5 = Radiobutton(root, text=setting5name, variable=selectionnumber, value=5, command=updatelable, font=("Century", 20), background=backgroundcolor, fg=textcolor)
R5.pack(anchor = W)

customfrequency=DoubleVar
customamplitude=DoubleVar
customlabel = Label(root, text = 'Set a Custom Frequency',font=("Century", 30), background=backgroundcolor, fg=textcolor)
customlabel = Label(root, text = 'Frequency',font=("Century", 20), background=backgroundcolor, fg=textcolor)
customlabel = Label(root, text = 'Amplitude',font=("Century", 20), background=backgroundcolor, fg=textcolor)
cfrequencyentry = Entry(root,textvariable = customfrequency,font=("Century", 20), background=backgroundcolor, fg=textcolor)
camplitudeentry = Entry(root,textvariable = customamplitude,font=("Century", 20), background=backgroundcolor, fg=textcolor)


root.mainloop()