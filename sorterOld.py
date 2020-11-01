from PIL import Image 
import os 
import fnmatch 
import shutil
import json
import PIL.ExifTags
import os
import gui

folderNameWhatsApp = "Bilder Whatsapp"
folderNameDoublePics = ""



# def doublePicSorter (picPath):
# #dir createt if not exist
#     rawPath = picPath 
#     if not os.path.exists(rawPath + folderNameDoublePics): 
#         os.mkdir(rawPath+folderNameDoublePics) 
#     os.listdir(path=rawPath) 

#     # list of pics in dir createt
#     list_PicsInDirectory = (fnmatch.filter(os.listdir(rawPath), '*.jpg')) 

#     print ('Es müssen '+ str(len(list_PicsInDirectory)) + ' Bilder miteinander verglichen werden') 

#     startLoop = 0 
#     i = 1 
#     h = 0 
#     bildZaehler = 0 

#     #check doublepics and move it to another folder
#     while startLoop < len(list_PicsInDirectory): 
#         while i  < len(list_PicsInDirectory): 
            
#             testImage1 = Image.open(rawPath+list_PicsInDirectory[h]).resize((10,10)).convert('RGB') 
#             pixels = list(testImage1.getdata()) 

#             testImage2 = Image.open(rawPath+list_PicsInDirectory[i]).resize((10,10)).convert('RGB') 
#             pixels2 = list(testImage2.getdata()) 

#             print ('Vergleiche ' + str(h) + ' mit '+ str(i)) 

#             if set(pixels) == set(pixels2):                 
#                 bildZaehler = bildZaehler + 1 
#                 shutil.move(rawPath+list_PicsInDirectory[h], rawPath+folderNameDoublePics) 
#                 list_PicsInDirectory.pop(h) 
#                 i = 1 
#                 h = 0 
#                 startLoop = 0 
                
#             else: 
#                 print ("nicht doppelt") 
#                 i = i + 1 
#         startLoop = startLoop + 1 
#         h = h + 1 
#         i = h + 1 

#     if bildZaehler == 0: 
#         print ('Programm beendet \n '+ 'Es gab keine doppelten Bilder') 
#     else: 
#         print ('Programm beendet \n' + 'Es wurden '+ str(bildZaehler) + ' doppelte Bilder erkannt und verschoben in '+ str(rawPath+folderNameDoublePics))

#return "test"

def whatsAppSorter(picPath):
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
                

        # startLoop = startLoop + 1 
        # h = h + 1 
        # i = h + 1 
        # h = i + 1

    if whatsAppPicCounter == 0: 
        print ('Programm beendet \n '+ 'Es gab keine WhatsApp Bilder') 
    else: 
        print ('Programm beendet\n' + 'Es wurden '+ str(whatsAppPicCounter) + ' Whatsapp Bilder erkannt und verschoben in '+ str(picPath+folderNameDoublePics))



