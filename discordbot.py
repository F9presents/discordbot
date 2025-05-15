import discord 
import os
import subprocess

__author__ = "F9"
__github__ = "https://github.com/F9presents"
__description__ = "This is a discord bot multi tool that can send messages to a discord channel and name your discord bot."
__version__ = "1.0.0"


discord_webhook = "discord_webhook"  # Replace with your actual Discord webhook 

print ("discord bot multi tool")
print ("{1} sned message to discord and how many time u wanna send it")
print ("{2} name ur discord bot")
while True:
    choice = input("Enter your choice: 1 or 2: ")
    if choice == "1":
        message = input("Enter the message you want to send: ")
        count = int(input("Enter the number of times you want to send the message: "))
        for i in range(count):
            subprocess.run(["curl", "-X", "POST", discord_webhook, "-H", "Content-Type: application/json", "-d", f'{{"content": "{message}"}}'])
            print(f"Message sent {i+1} times")
    elif choice == "2":
        bot_name = input("Enter the name of your Discord bot: ")
        print(f"Your Discord bot is named: {bot_name}")
    else:
        print("Invalid choice. Please enter 1 or 2.")


