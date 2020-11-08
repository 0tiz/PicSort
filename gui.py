from tkinter import *
import tkinter.filedialog
from PIL import Image 
import os 
import fnmatch 
import shutil
import PIL.ExifTags
import os
import sorter


folderNameWhatsApp = "Bilder Whatsapp"
# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt

# Funktionuiert aber der WErt in FolderPath wird nicht angepasst
def button_getPath():
    global folderPath
    test = tkinter.filedialog.askdirectory()
    pfadAnzeige.config(text=test)
    folderPath = str(test + "/")
    print (folderPath)

def start_button():

    try:
        sorter.whatsAppSorter(folderPath)
    except NameError:
        print("Bitte wähle einen Ordner")
    except FileNotFoundError:
        print("Es befinden sich keine Bilder in diesem Ordner")

fenster = tkinter.Tk()

fenster.title("PicSor")

# Label und Buttons erstellen.
getPath_button =        Button(fenster,text="Ordnerwahl",command=button_getPath)
exit_button =           Button(fenster,text="Beenden"   , command=fenster.quit)
start_button =          Button(fenster,text= "Start"    ,command=start_button)

pfadAnzeige = Label(text="Kein Order gewählt")




# Nun fügen wir die Komponenten unserem fenster 
# in der gwünschten Reihenfolge hinzu.
pfadAnzeige.pack()
getPath_button.pack()
start_button.pack()
exit_button.pack()





# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()



















































# import tkinter.filedialog
     
# tkinter.filedialog.asksaveasfilename()
# tkinter.filedialog.asksaveasfile()
# tkinter.filedialog.askopenfilename()
# tkinter.filedialog.askopenfile()
# tkinter.filedialog.askdirectory()
# tkinter.filedialog.askopenfilenames()
# tkinter.filedialog.askopenfiles()