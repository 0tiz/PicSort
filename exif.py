import json
import PIL.ExifTags
import os
import fnmatch
import shutil
from PIL import Image
import time



# img = PIL.Image.open()
# exif_data = img._getexif()



# def whatsAppSorter(picPath):


#     if not os.path.exists(picPath + "Bilder WhatsApp"): 
#         os.mkdir(picPath+"Bilder WhatsApp") 
#     os.listdir(path=picPath) 

#     list_PicsInDirectory = (fnmatch.filter(os.listdir(picPath), '*.jpg')) 

# # if exif_data is None:
# #    pack den scheiss in Whatsapp ordner


#     startLoop = 0 
#     i = 1 
#     h = 0 
#     bildZaehler = 0 
#     while startLoop < len(list_PicsInDirectory): 
#         while i  < len(list_PicsInDirectory): 

#             img = Image.open(picPath + list_PicsInDirectory[h])
#             exif_data = img._getexif()
#             img.close()

#             print (exif_data)

#             if exif_data is None:
#                 shutil.move(picPath+list_PicsInDirectory[h], picPath + "Bilder WhatsApp")
#                 bildZaehler = bildZaehler + 1


                    
#             else: 
#                 print ("kein Whatsapp Bild") 
#                 i = i + 1 

#             # startLoop = startLoop + 1 
#             # h = h + 1 
#             # i = h + 1 
        
#         if bildZaehler == 0: 
#             print ('Programm beendet \n '+ 'Es gab keine doppelten Bilder') 
#         else: 
#             print ('Programm beendet \n' + 'Es wurden '+ str(bildZaehler) + ' Whatsapp Bilder erkannt und verschoben in '+ str(picPath+"doppelte_bilder"))

#         return "test"

