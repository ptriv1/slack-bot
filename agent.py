import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def format_messages_for_prompt(messages):
    return "\n".join(
        f"[{msg['timestamp']}] {msg['user']}: {msg['text']}"
        for msg in messages
    )

def agent_decide_action(messages):
    prompt = [
        {
            "role": "system",
            "content": (
                "You are an autonomous assistant monitoring Slack conversations. "
                "Based on the messages provided, choose the most appropriate action from the following list:\n\n"
                "summarize_messages - Condense recent Slack messages into a summary\n"
                "post_to_slack - Share the summary or insights into a channel or DM\n"
                "detect_topic - Identify the main subject(s) being discussed\n"
                "wait_for_more_data - Choose to do nothing yet\n"
                "flag_follow_up - Mark certain messages as needing a human response\n\n"
                "Think step-by-step. Choose one ACTION and explain why.\n"
                "Respond in the format:\n"
                "ACTION: <action_name>\nREASON: <reasoning>"
            )
        },
        {
            "role": "user",
            "content": format_messages_for_prompt(messages)
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=prompt
    )
    
    content = response.choices[0].message.content
    lines = content.strip().splitlines()
    
    action_line = next((line for line in lines if line.startswith("ACTION:")), "")
    action = action_line.replace("ACTION:", "").strip()
    
    return action
