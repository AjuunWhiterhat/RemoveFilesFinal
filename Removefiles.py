import os
import shutil
import time

path = input("Enter the path of the old files that needs deletion: ")
folder = input("Enter the specific folder to be deleted: ")
days = 30

seconds = time.time()-(days*24*60*60)
print(seconds)

if os.path.exists(path):
    print("Path Exists")
    listFiles = os.listdir(path)

    print(listFiles)

    final = os.path.join(path,folder)
    print(final)


    ctime = os.stat(final).st_ctime
    print(ctime)
    
    
    if ctime > seconds:
        shutil.rmtree(final)
        print("Files removed successfully")





else:
    print("Error! Path not found")



    


