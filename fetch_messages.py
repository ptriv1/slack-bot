import os
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()  
client = WebClient(token=os.environ['SLACK_API_TOKEN'])

channel = input("Which channel do you want to search? ")

channels = client.conversations_list()['channels']