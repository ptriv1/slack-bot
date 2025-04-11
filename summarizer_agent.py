import os
from dotenv import load_dotenv
from fetch_messages import fetch_messages
from openai import OpenAI

load_dotenv()  
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

channel_name = input("Which channel do you want to search? ")
messages = fetch_messages(channel_name)

def summarize_messages(messages):
    message_text = "\n".join(
        f"[{msg['timestamp']}] {msg['user']}: {msg['text']}"
        for msg in messages
    )

    prompt = [
        {"role": "system", "content": "You are a helpful assistant that summarizes Slack conversations."},
        {"role": "user", "content": f"Summarize the following Slack messages:\n\n{message_text}"}
    ]
    response = client.chat.completions.create(
       model="gpt-4",
       messages=prompt 
    )

    summary = response.choices[0].message.content
    return summary

summary = summarize_messages(messages)

with open("summary.txt", "w") as file:
    file.write(summary)