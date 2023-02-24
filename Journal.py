#!/usr/bin/python3
import os, time
from datetime import date

response = input("Hey User! How are you feeling today?\n")
current_date = date.today()
formatted_date = current_date.strftime("%B %d, %Y")

if response.lower() == "good":
	print("Glad to hear that")
	time.sleep(0.5)
	print("Let's get to work then shall we?")
else:
	print("Well... Let's get some work done.")
with open("Journal.txt", "a") as J:
	J.write("\n" + formatted_date + "\n" + response + "\n----\n")
