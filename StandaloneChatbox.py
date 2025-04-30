import os
import platform
import time
import shutil
import sys
import json
import random
import requests as re
from datetime import datetime
# importing module python has built in
randommessage = [
	"randommessage1",
	"randommessage2",
	"randommessage3"
]

animatedmessage = []
index = 0

try:
	from pythonosc import udp_client
except:
	print('Could not import python-osc, would you like to install it? (y/n)')
	e = input("Answer: ")
	if e.lower() == "y":
		os.system("pip install python-osc")
		try:
			from pythonosc import udp_client
			input("sucessfuly installed python-osc! Press any key to proceed\n")
		except:
			print("An error has occured")
	else:
		exit(1)

try:
	import argparse
except:
	print('Could not import argparse, would you like to install it? (y/n)')
	e = input("Answer: ")
	if e.lower() == "y":
		os.system("pip install argparse")
		try:
			import argparse
			input("sucessfuly installed argparse! Press any key to proceed\n")
		except:
			print("An error has occured")
	else:
		exit(1)
# attempts to import pythonosc and argsparge, if it fails it asks the user if it wants to install

parser = argparse.ArgumentParser(description="A VRChat OSC script by daepikgoose")
parser.add_argument('--quick-start', action='store_true', help="Instantly starts the script without going to the main menu")
args = parser.parse_args()

def clear():
	if sys.platform.lower() == "linux":
		os.system("clear")
	else:
		os.system("cls")
# making a clear function to clear the terminal

configfolder = "scbconfig"
headsetip = f"{configfolder}/ip"
messagefile = f"{configfolder}/message"
updaterate = f"{configfolder}/updaterate"
animatedtextfile = f"{configfolder}/animatedtext"
tinychat = f"{configfolder}/tinychat"
thinchatunicodes = "\u0003\u001f"
version_url = "https://raw.githubusercontent.com/Daepikgoose/Standalone-Chatbox/refs/heads/main/version"
version = 1.3
latestversion = re.get(version_url).text

system_name = platform.system()
	
if system_name == 'Windows':
	currentos =  "Windows"
else:
	currentos = "Unknown"
if 'ANDROID_DATA' in os.environ and currentos == "Unknown":
    currentos = "Android"
else:
    if currentos == "Unknown":
        currentos = "Linux"
# setting up variables


if not os.path.exists(configfolder):
	os.makedirs(configfolder)

if not os.path.isfile(headsetip):
	with open(headsetip, 'w') as file:
		file.write('127.0.0.1')

if not os.path.isfile(updaterate):
	with open(updaterate, 'w') as file:
		file.write('1.5')

if not os.path.isfile(messagefile):
	with open(messagefile, 'w') as file:
		file.write(r'{hour}:{minute}\Update rate: {updaterate}')

if not os.path.isfile(animatedtextfile):
	with open(animatedtextfile, 'w') as file:
		file.write('text1\ntext2\ntext3')

if not os.path.isfile(tinychat):
	with open(tinychat, 'w') as file:
		file.write('0')
# setting up the config folder and files if they dont exist


with open(messagefile, 'r') as file:
		message = file.read()

with open(headsetip, 'r') as file:
		ip = file.read()

with open(updaterate, 'r') as file:
	updatedelay = file.read()

with open(tinychat, 'r') as file:
	if file.read() == "0":
		thinchat = False
	else:
		thinchat = True

with open(animatedtextfile, 'r') as file:
	for line in file:
		line = line.strip()
		if not line:
			continue
		animatedmessage.append(line)

def switchmenu(n):
	if n == "0":
		clear()
		mainmenu()
	elif n == "1":
		clear()
		configmenu()
	elif n == "2":
		startscript(ip, message)
	elif n == "3":
		clear()
		infomenu()
	else:
		mainmenu()


def editconfig(w, v):
	global ip, message, updatedelay, thinchat
	if w == "1":
		with open(headsetip, 'w') as file:
			file.write(v)
		ip = v
		input("Value edited, press any key to go back")
		switchmenu(1)
	elif w == "2":
		with open(messagefile, 'w') as file:
			file.write(v)
		message = v
		input("Value edited, press any key to go back")
		switchmenu(1)
	elif w == "3":
		with open(updaterate, 'w') as file:
			file.write(v)
		updatedelay = v
		input("Value edited, press any key to go back")
		switchmenu(1)
	elif w == "4":
		if thinchat == False:
			thinchat = True
			with open(tinychat, 'w') as file:
				file.write("1")
		else:
			thinchat = False
			with open(tinychat, 'w') as file:
				file.write("0")
			


def mainmenu():
	clear()
	print("Standalone Chatbox".center(shutil.get_terminal_size().columns))
	print("Main menu".center(shutil.get_terminal_size().columns))
	print("\n\n")
	print("1. Edit config".center(shutil.get_terminal_size().columns))
	print("2. Launch script".center(shutil.get_terminal_size().columns))
	print("3. Info".center(shutil.get_terminal_size().columns))
	print("\n\n")
	choice = input("Choice: ")
	switchmenu(choice)


def configmenu():
	print("Standalone Chatbox".center(shutil.get_terminal_size().columns))
	print("Config editor".center(shutil.get_terminal_size().columns))
	print("\n\n")
	print("1. Edit headset ip".center(shutil.get_terminal_size().columns))
	print("2. Edit message".center(shutil.get_terminal_size().columns))
	print("3. Edit update rate".center(shutil.get_terminal_size().columns))
	print("4. Toggle thin chat".center(shutil.get_terminal_size().columns))
	print("5. Back to main menu".center(shutil.get_terminal_size().columns))
	choice = input("Choice: ")
	if choice in ("1", "2", "3"):
		value = input("New value: ")
		editconfig(choice, value)
	elif choice == "4":
		editconfig("4", "Useless text")
		switchmenu(1)
	elif choice == "5":
		switchmenu(0)
	else:
		switchmenu(1)

def infomenu():
	print("Standalone Chatbox".center(shutil.get_terminal_size().columns))
	print("Info".center(shutil.get_terminal_size().columns))
	print("\n\n")
	print("Made by daepikgoose on discord".center(shutil.get_terminal_size().columns))
	print("Discord server: https://discord.gg/DaefaRaHAv".center(shutil.get_terminal_size().columns))
	print("\n")
	print(f"Device ip: {ip}".center(shutil.get_terminal_size().columns))
	print(f"Message: {message}".center(shutil.get_terminal_size().columns))
	print(f"Update rate: {updatedelay}".center(shutil.get_terminal_size().columns))
	print(f"Thin chat: {thinchat}".center(shutil.get_terminal_size().columns))
	input("Press any key to go back")
	switchmenu(0)

def startscript(i, m):
	global index
	client = udp_client.SimpleUDPClient(ip, 9000)
	print("Press ctrl then c to cancel the script")
	while True:
		infoformat = (
	message
	.replace("{hour}", datetime.now().strftime('%H'))
	.replace("{minute}", datetime.now().strftime('%M'))
	.replace("{updaterate}", updatedelay)
	.replace("{randommessage}", random.choice(randommessage))
	.replace("{animatedmessage}", animatedmessage[index])
	.replace("{currentos}", currentos)
	.replace("\\n", "\n")
)
		if thinchat == True:
			client.send_message("/chatbox/input", [infoformat+thinchatunicodes, True, False])
		else:
			client.send_message("/chatbox/input", [infoformat, True, False])
		time.sleep(float(updatedelay))
		index = (index + 1) % len(animatedmessage)

if float(latestversion) > version:
	input("New version available! Please download the new file. Press any key to proceed to menu")

if args.quick_start:
    startscript(ip, message)
else:
    mainmenu()