# Discord-Synchronized-Messaging

## What is it?
I created a simple system for Discord bots to send messages one after eachother in an organized sequence.
In this case, I used it to play a series of ascii frames grabbed from a text file.

## How to use it?
Firstly, enter the ids of your bots into the bot_ids list at the top, without quotations around them.
Now fill up your text file with what you want each message to be, with a "\`" between each message.
Next, run the script for each bot with: 
   python3 asciivideo.py TOKEN
Since the token is an argument you can pass into the command line, to run three bots, you could do:
   python3 asciivideo.py TOKEN1 & python3 asciivideo.py TOKEN2 & python3 asciivideo.py TOKEN3
All you have to do next is type .startascii in a text channel.

## Example
![asciivideoplayer](https://user-images.githubusercontent.com/22421950/113631015-0adb4d00-9626-11eb-82a1-c433d7b7d08b.gif)

