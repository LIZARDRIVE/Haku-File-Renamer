import os

def cleanup_folder(currpath):
    path = currpath
    for subdir, dirs, files in os.walk(path):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".epub"): # change for whatever extension you are using

                filename = (os.path.basename(filepath.replace("_", " ")).split())
                fileend=(filename[len(filename)-1]).replace(".epub", "")    
                
                newname=os.path.basename(subdir)+"_"+fileend.zfill(4)+".epub"        

                fullfilepath = subdir + '\\' + file        
                fullnewname = subdir + '\\' + newname
                
                if not os.path.exists(fullnewname): 
                    os.rename(r''+ fullfilepath + '',r'' + fullnewname + '')


mypath = r"C:\Users\...\Mangas" # adapt to your own configuration
folder_list=[]

folder_list.append("Berserk")
folder_list.append("Akira")
folder_list.append("Jujutsu Kaisen")
folder_list.append("Hunter x Hunter")
folder_list.append("Kingdom")
# remove or add entries following 5 examples above


for i in folder_list:
    print(mypath+ '\\' + i)
    cleanup_folder(mypath+ '\\' + i)
