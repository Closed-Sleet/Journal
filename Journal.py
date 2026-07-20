#ADA
#Journal.py A Command Line Journaling tool

#Initializing required variables
import os, time, datetime
current_date = datetime.datetime.now(tz=None)
formatted_date = current_date.strftime("%A, %B %d, %Y \n%I:%M%p\n")

#Taking input from terminal
fileName = input("\nWhere would you like to put this entry?\n")
response = input("Type entry now. Press enter when you're done.\n")

#Appending to the Input FileName
with open(fileName +'.txt', 'a') as J:
	J.write("\n" + formatted_date + "\n" + response + "\n----\n")
print("\nEntry has been appended to " + fileName + ".txt")