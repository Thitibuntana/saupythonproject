import os

if os.path.exists("myfile01.txt") :
    os.remove("myfile01.txt")
else:
    print("No file found.")