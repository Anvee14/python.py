import os
import shutil
source = input("enter src folder name:")
dst = input("enter dst folder name:")
source = source +'/'
dst = dst+'/'
listOfFiles = os.listdir(source)
for file in listOfFiles :
    copy = shutil.copy((source+file),dst)
    
