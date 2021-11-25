import os
import time
import datetime

print("----------------------------------------------------------------")
print("FileName2Date")
print("converting from subfolder ./convert/")
print("----------------------------------------------------------------")
print("Select file name layout:")
print("[1] YYYY-MM-DD hh-mm-ss")
print("[2] YYYY-DD-MM hh-mm-ss")
print("[3] DD-MM-YYYY hh-mm-ss")
print("[4] MM-DD-YYYY hh-mm-ss")
print("or enter your own layout:")
layoutselection = input()
if (layoutselection=="1"):
    layout = "YYYY-MM-DD hh-mm-ss"
elif (layoutselection=="2"):
    layout = "YYYY-DD-MM hh-mm-ss"
elif (layoutselection=="3"):
    layout = "DD-MM-YYYY hh-mm-ss"
elif (layoutselection=="4"):
    layout = "MM-DD-YYYY hh-mm-ss"
else:
    layout = layoutselection
folderpath = "./convert/"
files = [f for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))]

for file in files:
    print("----------------------------------------------------------------")
    print(f"file: {file}")
    fileLocation = folderpath + "/" + file
    print(file[layout.find("YYYY"):layout.find("YYYY")+4])
    year = int(file[layout.find("YYYY"):layout.find("YYYY")+4])
    month = int(file[layout.find("MM"):layout.find("MM")+2])
    day = int(file[layout.find("DD"):layout.find("DD")+2])
    hour = int(file[layout.find("hh"):layout.find("hh")+2])
    minute = int(file[layout.find("mm"):layout.find("mm")+2])
    second = int(file[layout.find("ss"):layout.find("ss")+2])
    date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    modTime = time.mktime(date.timetuple())
    os.utime(fileLocation, (modTime, modTime))
    print(f"saved date {day}.{month}.{year} {hour}:{minute}:{second}")
print("----------------------------------------------------------------")