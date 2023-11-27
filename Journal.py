#!/usr/bin/python3
#Lantis T. Hegg
import os, time, datetime

print("Hello user! How are you feeling today?")
current_date = datetime.datetime.now(tz=None)
response = input("Type entry now. \nPress enter when you're done.\n")
formatted_date = current_date.strftime("%A, %B %d, %Y \n%I:%M%p\n")

if (" good " in response.lower()):
	print("Glad to hear")
	time.sleep(0.25)
	print("Let's get some work done\n")
else:
	print("Well, let's just get to work.\n")
time.sleep(0.1)

File = input("\nWhere would you like to put this entry?\n")

if not File:
	File = "Journal"

with open(File + '.txt', 'a') as J:
	J.write("\n" + formatted_date + "\n" + response + "\n----\n")
print("Entry has been put in " + File + ".txt")