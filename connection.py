"""
	This program show the IP of connected devices form Wi-Fi that your device connected with
"""
import os

bashCommand="nmap -sn 192.168.1.0/24"
os.system(bashCommand)

