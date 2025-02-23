import discord
import os
from dotenv import load_dotenv
import aiohttp
import json
url = "https://9959-116-75-221-16.ngrok-free.app" 

# def get_login_credentials():
#     with open('login_credentials.txt') as f:
#         credentials = f.read().splitlines()
#         dict_ = {}
#         for i in credentials:
#           dict[i.split(" ")[0]] = i.split(" ")[1] # second part will the accesss Token 
#     return dict_

# login_credentials = get_login_credentials()
load_dotenv()  # Load environment variables from .env

intents = discord.Intents.default()  # You can customize intents if needed
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user: #ignore if message is from the bot !
    return
  if (message.content.startswith('Hello')):
    await message.channel.send(f'nikal laude {message.author} , just trolling !')

  # if(message.content.startswith("Register")):
  #   try:
  #     username , password = message.content.split("Register")[1].split("_")
  #     headers = {"Content-Type": "application/json"}  # Explicitly set JSON header
  #     payload = json.dumps({"hash": flag})  # Convert payload to JSON string
  #     async with aiohttp.ClientSession() as session:
  #       try:
  #           async with session.post(url, data=payload, headers=headers) as response:
  #               content_type = response.headers.get("Content-Type", "")
  #               if "application/json" in content_type:  
  #                   response_json = await response.json()  # Parse JSON safely
  #                   print(response_json)
  #                   status = response_json.get("Status", "Unknown")
  #                   if status == 200:
                      
                    
        # except aiohttp.ClientError as e:
        #       await message.channel.send(f"Error connecting to API: `{str(e)}`")
      
    #   with open("login_credentials.txt","a") as f:
    #     f.writelines(f"{username} {password}\n")
    # except:
    #   await message.channel.send("Enter a Valid Username Or Password")
  if message.content.startswith("Flag"):
    
    flag = message.content.split("$Flag", 1)[-1].strip()
    if(flag=="" or flag==" ") :
      await message.channel.send("Please enter a valid Flag to verify")
      return
      
    headers = {"Content-Type": "application/json"}  # Explicitly set JSON header
    payload = json.dumps({"hash": flag})  # Convert payload to JSON string
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url+"/checkpassword", data=payload, headers=headers) as response:
                content_type = response.headers.get("Content-Type", "")

                if "application/json" in content_type:  
                    response_json = await response.json()  # Parse JSON safely
                    print(response_json)
                    status = response_json.get("Correct", "Unknown")
                    message_text = response_json.get("flag", "No message provided")
                    if(status):
                      await message.channel.send("Correct Here is Your flag: "+message_text)
                    else:
                      await messsage.channel.send("Incorrect Here is YOur flag"+message_text)
        except aiohttp.ClientError as e:
              await message.channel.send(f"Error connecting to API: `{str(e)}`")
          
  if message.content.startswith('Help'):
    await message.channel.send('''
    $Hello - Say hello to the bot
    To Register Yourself send $Register<username>_<password>
    To get Verify flag Send $Flag<flag>
    ~Made by @0xZ15H4N, chao~
    ''')

  if message.content.startswith("Commands"): 
    await message.channel.send('Here are the commands I can respond to: Hello, Help, Commands, Flag, Register, Login')

client.run(os.getenv("TOKEN"))


