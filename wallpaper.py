import os
from array import *
import time
from random import randint

#a = array('i',os.listdir("/home/vigilante/Pictures")
mylist = os.listdir("/home/vigilante/Pictures")
while(True):
    x=randint(0,len(mylist));
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/vigilante/Pictures/"+str(mylist[x]))
    print(mylist[x])
    time.sleep(10)  # sleep 2 seconds between each print
