from PIL import Image 
import os 
import fnmatch 
import shutil
import PIL.ExifTags
import os




def whatsAppSorter(picPath):
    folderNameWhatsApp = "WhatsApp Bilder"
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
        break
    print("Es wurden " + str(whatsAppPicCounter) + " WhatsApp Bilder verschoben")