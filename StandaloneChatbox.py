import os
import time
import shutil
import json
import random
import requests as re
from datetime import datetime
# importing module python has built in
randomfact = [
    "A hippopotamus can run faster than a man.",
    "A crocodile cannot stick its tongue out.",
    "Most insects hatch from eggs.",
    "Pigs can’t look up into the sky – it’s physically impossible.",
    "The shark is the only fish that can blink with both eyes.",
    "An ostrich’s eye is bigger than its whole brain.",
    "Kangaroos can’t walk backward.",
    "Avocados are a fruit, not a vegetable.",
    "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion meaning the iron heats up, the particles gain kinetic energy and take up more space.",
    "Trypophobia is the fear of closely-packed holes.",
    "Australia is wider than the moon.",
    "A cockroach can live for up to one week without its head.",
    "It is impossible for most people to lick their own elbow.",
    "A crocodile cannot stick its tongue out.",
    "A shrimp’s heart is in its head.",
    "The “sixth sick sheik’s sixth sheep’s sick” is believed to be the toughest tongue twister in the English language.",
    "If you sneeze too hard, you could fracture a rib.",
    "Wearing headphones for just an hour could increase the bacteria in your ear by 700 times.",
    "In the course of an average lifetime, while sleeping you might eat around 70 assorted insects and 10 spiders, or more.",
    "Some lipsticks contain fish scales.",
    "Cat urine glows under a black-light.",
    "Like fingerprints, everyone’s tongue print is different.",
    "Rubber bands last longer when refrigerated.",
    "There are 293 ways to make change for a dollar.",
    "The average person’s left hand does 56% of the typing (when using the proper position of the hands on the keyboard; Hunting and pecking doesn’t count!).",
    "A shark is the only known fish that can blink with both eyes.",
    "The longest one-syllable words in the English language are “scraunched” and “strengthed.” Some suggest that “squirreled” could be included, but squirrel is intended to be pronounced as two syllables (squir-rel) according to most dictionaries. “Screeched” and “strengths” are two other long one-syllable words, but they only have 9 letters.",
    "“Dreamt” is the only English word that ends in the letters “mt”.",
    "Almonds are a member of the peach family.",
    "There are only four words in the English language which end in “dous”: tremendous, horrendous, stupendous, and hazardous.",
    "Los Angeles’ full name is “El Pueblo de Nuestra Senora la Reina de los Angeles de Porciuncula.”",
    "A cat has 32 muscles in each ear.",
    "Tigers have striped skin, not just striped fur.",
    "In many advertisements, the time displayed on a watch is 10:10.",
    "The characters Bert and Ernie on Sesame Street were named after Bert the cop and Ernie the taxi driver in Frank Capra’s “It’s a Wonderful Life.”",
    "The giant squid has the largest eyes in the world.",
    "Most people fall asleep in seven minutes.",
    "“Stewardesses” is the longest word that is typed with only the left hand.",
    "Camels have three eyelids.",
    "Mosquitos are attracted to people who just ate bananas.",
    "Cats have more than 100 vocal cords.",
    "A snail breathes through its foot.",
    "Fish cough.",
    "Elephants are the only mammal that can’t jump.",
    "Oysters can change from one gender to another (and back again).",
    "Dead people can get goosebumps.",
    "The only letter that doesn’t appear on the periodic table is J.",
    "The tallest man in recorded history was 8’11.",
    "The unique smell of rain actually comes from plant oils, bacteria, and ozone.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old and still edible.",
    "An octopus has three hearts.",
    "A cloud can weigh more than a million pounds.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted 38 minutes.",
    "Bananas are berries, but strawberries are not.",
    "A day on Venus is longer than a year on Venus.",
    "Cows have best friends and can become stressed when separated from them.",
    "The moon is slowly moving away from Earth at a rate of 1.5 inches per year.",
    "There are more stars in the universe than grains of sand on all of Earth's beaches.",
    "The longest hiccuping spree lasted 68 years.",
    "Wombat poop is cube-shaped.",
    "You can’t hum while holding your nose.",
    "Sharks have been around longer than trees.",
    "The longest recorded flight of a chicken is 13 seconds.",
    "The shortest commercial flight in the world is between two islands in Scotland, lasting just 57 seconds.",
    "A jiffy is an actual unit of time, equaling 1/100th of a second.",
    "A duck’s quack doesn’t echo, and no one knows why.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "A mole can dig a tunnel 300 feet long in a single night.",
    "A jigsaw puzzle was invented in 1767 by a mapmaker named John Spilsbury.",
    "Sloths can hold their breath for up to 40 minutes underwater.",
    "The first product to have a barcode was Wrigley’s gum.",
    "A day on Mars is just 40 minutes longer than a day on Earth.",
    "In Japan, there are more pets than children.",
    "There’s a species of jellyfish that is biologically immortal.",
    "Walt Disney holds the record for the most Academy Awards, with 22 wins.",
    "The longest hiccuping streak lasted 68 years.",
    "You share your birthday with at least 9 million other people in the world.",
    "An adult human body has 206 bones, but babies are born with about 270 bones.",
    "Some turtles can breathe through their butts.",
    "The longest wedding veil was the same length as 63.5 football fields.",
    "Penguins propose to their mates with a pebble.",
    "A person can live without food for about a month, but only about a week without water.",
    "The oldest living animal on Earth is a 507-year-old clam named Ming.",
    "Some cats are allergic to humans.",
    "A group of flamingos is called a 'flamboyance.'",
    "A sneeze can travel up to 100 miles per hour.",
    "Most lipstick contains fish scales.",
    "The Eiffel Tower can grow taller by about 6 inches in the summer.",
    "The national animal of Scotland is the unicorn.",
    "Dolphins have names for each other.",
    "The only continent without a desert is Europe.",
    "Sharks are older than trees.",
    "One in every 200 men is a direct descendant of Genghis Khan.",
    "The average person walks the equivalent of three times around the world in a lifetime.",
    "The world’s largest snowflake on record was 15 inches wide and 8 inches thick.",
    "Cows can produce more milk when listening to music.",
    "The longest living insect is the termite queen, which can live up to 50 years.",
    "Butterflies taste with their feet.",
    "Cows can recognize faces, even from photos.",
    "The first alarm clock could only ring at 4 a.m.",
    "The human nose can detect over 1 trillion different scents.",
    "In space, astronauts can't cry because there’s no gravity to make the tears fall."
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

# attempts to import pythonosc, if it fails it asks the user if it wants to install

def clear():
	os.system("clear")
# making a clear function to clear the terminal

configfolder = "scbconfig"
headsetip = f"{configfolder}/ip"
messagefile = f"{configfolder}/message"
updaterate = f"{configfolder}/updaterate"
animatedtextfile = f"{configfolder}/animatedtext"
version_url = "https://pastebin.com/raw/sjqiyq82"
version = 1
latestversion = re.get(version_url).text
# setting up starter variables


if not os.path.exists(configfolder):
	os.makedirs(configfolder)

if not os.path.isfile(headsetip):
    with open(headsetip, 'w') as file:
        file.write('127.0.0.1')

if not os.path.isfile(updaterate):
    with open(updaterate, 'w') as file:
        file.write('3')

if not os.path.isfile(messagefile):
    with open(messagefile, 'w') as file:
        file.write(r'{hour}:{minute}\Update rate: {updaterate}')

if not os.path.isfile(animatedtextfile):
    with open(animatedtextfile, 'w') as file:
        file.write('text1\ntext2\ntext3')
# setting up the config folder and files if they dont exist


with open(messagefile, 'r') as file:
        message = file.read()

with open(headsetip, 'r') as file:
        ip = file.read()

with open(updaterate, 'r') as file:
	updatedelay = file.read()

with open(animatedtextfile, 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        animatedmessage.append(line)


# the useful variables


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
	global ip, message, updatedelay
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
	print("4. Back to main menu".center(shutil.get_terminal_size().columns))
	choice = input("Choice: ")
	if choice == "1" or "2" or "3":
		value = input("New value: ")
		editconfig(choice, value)
	elif choice == "4":
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
    .replace("{randomfact}", random.choice(randomfact))
    .replace("{animatedmessage}", animatedmessage[index])
    .replace("\\n", "\n")
)
		client.send_message("/chatbox/input", [infoformat, True, False])
		time.sleep(float(updatedelay))
		index = (index + 1) % len(animatedmessage)

if float(latestversion) > version:
	input("New version available! Please download the new file. Press any key to proceed to menu")

mainmenu()