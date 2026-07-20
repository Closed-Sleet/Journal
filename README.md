# Journal.py
## A Command Line Journaling tool made in Python.

## What it does
It takes your input entry, file name, and the date/time. By default it uses Journal.txt
The file it writes to will be created if not already present and it just appends the entry to the end.
The file has to be in the same directory of Journal.py itself otherwise it will create the file in the directory.
To read your journal just open up your text file in your prefered text editor.

## Dependencies
Ensure you have the full python3 library.
```sudo apt-get install python3```

## Linux users
Remember to use ```chmod +x Journal.py``` so you can run it. (or other permissions where applicable)
Run the script using ```./Journal.py``` in the terminal window.

## Windows users
Remember to install python properly and ensure the script is in the folder you want the txt files to go.
*Honestly don't know why a windows user would need a command line tool but it is functional.*

## Why?
I mainly made this script cause I was bored, but also it does serve a genuine purpose.
This automatically formats the entries with the date and time and avoids having to scroll through long files to write at the end of it.
I usually need to write things down to remember them, while for the longest time I've been using google docs,
that's proven unreliable now that I am without internet often. Which is usually when I want to write.
This script is mainly to make it easier to format these things and look back on.

I may consider making a proper application out of this at somepoint but for now it's reliant on a terminal window.