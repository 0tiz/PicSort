from tkinter import *
import tkinter.filedialog
from PIL import Image 
import os 
import fnmatch 
import shutil
import PIL.ExifTags
import os

picPath = "D:/Sortierer/"
folderNameWhatsApp = "Bilder Whatsapp"
# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt

def whatsAppSorter(picPath=picPath):
    #dir createt if not exist   
    if not os.path.exists(picPath + folderNameWhatsApp):
        os.mkdir(picPath+folderNameWhatsApp) 
        os.listdir(path=picPath) 

    #create a vluelist of pics in dir
    list_PicsInDirectory = (fnmatch.filter(os.listdir(picPath), '*.jpg'))

    startLoop = 0 
    i = 0
    h = 0 
    whatsAppPicCounter = 0 

    while startLoop < len(list_PicsInDirectory): 
        while i  < len(list_PicsInDirectory): 
            
            #check if exifData exist
            img = Image.open(picPath + list_PicsInDirectory[h])
            exif_data = img._getexif()
            img.close()

            print (exif_data)

            if exif_data is None:
                shutil.move(picPath+list_PicsInDirectory[h], picPath + folderNameWhatsApp)
                whatsAppPicCounter = whatsAppPicCounter + 1
                list_PicsInDirectory.pop(h) 
                i = 0 
                h = 0 
                startLoop = 0 

            else: 
                print ("kein Whatsapp Bild") 
                i = i + 1
                h = i
                
    if whatsAppPicCounter == 0: 
        print ('Programm beendet \n '+ 'Es gab keine WhatsApp Bilder') 
    else: 
        print ('Programm beendet\n' + 'Es wurden '+ str(whatsAppPicCounter) + ' Whatsapp Bilder erkannt und verschoben in '+ str(picPath+folderNameDoublePics))


def button_getPath():
    test = tkinter.filedialog.askdirectory()
    pfadAnzeige.config(text=test)
    picPath = test + "/"




# Ein fenster erstellen
fenster = tkinter.Tk()
# fenster.geometry(500*500)
# Den fenstertitle erstellen
fenster.title("PicSor")

# Label und Buttons erstellen.
getPath_button =        Button(fenster,text="Ordnerwahl",command=button_getPath)
startProgram_button =   Button(fenster,text="Start"     ,command=whatsAppSorter)
exit_button =           Button(fenster,text="Beenden"   , command=fenster.quit)

pfadAnzeige = Label(text="Kein Order gewählt")


# Nun fügen wir die Komponenten unserem fenster 
# in der gwünschten Reihenfolge hinzu.
pfadAnzeige.pack()
getPath_button.pack()
startProgram_button.pack()
exit_button.pack()



# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()

test = getPath_button
print (test)


















































# import tkinter.filedialog
     
# tkinter.filedialog.asksaveasfilename()
# tkinter.filedialog.asksaveasfile()
# tkinter.filedialog.askopenfilename()
# tkinter.filedialog.askopenfile()
# tkinter.filedialog.askdirectory()
# tkinter.filedialog.askopenfilenames()
# tkinter.filedialog.askopenfiles()