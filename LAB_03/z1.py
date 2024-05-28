import glob
import os
import shutil

input = "zadanie1"

try:
    os.mkdir(input + "_wynik")
except:
    pass

files = glob.glob(input + "/*", recursive=True)
for file in files:
    #WINDOWS
    #wyraz = file.split("\\")

    #LINUX / MACOS
    wyraz = file.split("/")

    try:
        os.mkdir(input + "_wynik/"+wyraz[1][0].upper())
    except:
        pass
    print(wyraz)
    shutil.copy(file, input + "_wynik/" + wyraz[1][0].upper() + "/" + wyraz[1])
