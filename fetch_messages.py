import os
import json
from datetime import datetime
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()  

client = WebClient(token=os.environ['SLACK_API_TOKEN'])

channel_name = input("Which channel do you want to search? ")

channels = client.conversations_list()['channels']

channel_id = None

for channel in channels:
    if channel['name'] == channel_name:
        channel_id = channel['id']

if not channel_id:
    print("Channel not found. Please check the name and try again.")
    exit()

result = client.conversations_history(channel=channel_id)

formatted_messages = []

for message in result['messages']:
    text = message.get('text', '[no text]')
    ts = message.get('ts', None)
    user = message.get('user', '[unknown user]')

    if ts:
        readable_time = datetime.fromtimestamp(float(ts)).strftime('%Y-%m-%d %H:%M:%S')
    else:
        readable_time = '[no timestamp]'

    formatted_messages.append({
        "timestamp": readable_time,
        "text": text,
        "user": user
    })

with open("messages.json", "w") as file:
    json.dump(formatted_messages, file, indent=2)