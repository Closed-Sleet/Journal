# Journal.py
A journal type thing for linux using the terminal.
It takes your input and the date and time, then prompts you for the filename you wish to append your entry to. By default it uses Journal.txt
The file it writes to will be created if not already present and it won't override text in the file, just appends the entry to it.
The file has to be in the same directory and Journal.py itself otherwise it will create the file in the directory.
to read your journal just open up your text file in your prefered text editor.

## Dependencies
Ensure you have the full python3 library.
```sudo apt-get install python3```

## Debian based linux
Remember to use ```chmod +x Journal.py``` so you can run it.
Run the script using ```./Journal.py``` in the terminal window.

## Why?
I mainly made this script cause I was bored, but also it does serve a genuine purpose.
This automatically formats the entries with the date and time and avoids having to scroll through long files to write at the end of it.
I usually need to write things down to remember them, while for the longest time I've been using a google doc,
that's proven unreliable now that I am without internet often. Which is usually when I want to write.
This script is mainly to make it easier to format these things and look back on.

I may consider making a proper application out of this at somepoint but for now it's reliant on a terminal window.
