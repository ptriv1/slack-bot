import os
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()  
client = WebClient(token=os.environ['SLACK_API_TOKEN'])
