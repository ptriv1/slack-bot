import os
from dotenv import load_dotenv
from fetch_messages import fetch_messages
import openai

load_dotenv()  
openai.api_key = os.environ["OPENAI_API_KEY"]

channel_name = input("Which channel do you want to search? ")
messages = fetch_messages(channel_name)
