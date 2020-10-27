from tkinter import *
import tkinter.filedialog
import sorter



# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button anklickt
def save_filepath():
    sorter.folderNameWhatsApp = tkinter.filedialog.askdirectory()
    return filepath

def start_program():
    sorter.whatsAppSorter(save_filepath)



# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("PicSorter")

# Label und Buttons erstellen.
change_button = Button(fenster, text="Ändern", command=save_filepath)
start_button = Button(fenster, text = "Start", command=start_program)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)


anweisungs_label = Label(fenster, text="Wähle einen Ordner, der sortiert werden soll")

info_label = Label(fenster, text="Ich bin eine Info:\n\
Der Beenden Button schliesst das Programm.")

# Nun fügen wir die Komponenten unserem Fenster 
# in der gwünschten Reihenfolge hinzu.
anweisungs_label.pack()
change_button.pack()
info_label.pack()
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