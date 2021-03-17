# importing the module 
import wikipedia  
import requests
import time

#User Input
channel = str(input("Enter Destination of Spam: "))
spammer = ("https://discord.com/api/v8/channels/"+channel+"/messages")

#Bot Works Confirmation
print("Bot Activated: Check Discord")

#Wikepedia Results fetched
result = wikipedia.summary("League of Legends", sentences = 20)

#Taking results make list
WikiList = result.split()

#Printing Each individual item in list to console and Discord
for item in WikiList:
    payload = {'content' : "<@!> " + " :flushed:" + item + ":flushed:"}
    header = {'authorization' : ""}
    print(item)
    r =  requests.post(spammer, data=payload, headers=header)
    time.sleep(0.75)
