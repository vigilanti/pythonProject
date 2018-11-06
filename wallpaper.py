#This program demonstrate how to change wallpaper in Linux distrubition within 10 second

import os
from array import *
import time
from random import randint

mylist = os.listdir("/home/vigilante/Pictures")#path to directory containing Pictures
while(True):
    x=randint(0,len(mylist));
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/vigilante/Pictures/"+str(mylist[x]))
    print(mylist[x])
    time.sleep(10)  # sleep 2 seconds between each print
