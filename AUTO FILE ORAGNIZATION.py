import os
import os.path
import shutil
import gui

source = gui.source   #it will come from GUI.py
destination = gui.destination  # it will come from GUI.py

source += '\\' 
destination += '\\'

for i in os.listdir(source):
    split_tup = os.path.splitext(i)
    extension=split_tup[1]
    extension = extension[1:]

    if extension == '':
        continue 
    
    if not(os.path.isdir(destination + extension)):
        path = os.path.join(destination, extension)
        os.mkdir(path)

    s = source + i
    d = destination + extension + '\\' + i

    if os.path.exists(d):
        print(i,"already exist")
        continue
    
    shutil.move(s, d)