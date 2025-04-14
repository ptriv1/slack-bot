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

def post_to_slack(channel, text):
    from slack_sdk import WebClient
    import os
    client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
    client.chat_postMessage(channel=channel, text=text)

def detect_topic(messages):
    # Optional LLM prompt or heuristic
    return "Main topic: [placeholder]"

def wait_for_more_data(_):
    return "Agent has decided to wait."

def flag_follow_up(messages):
    return "Flagged messages needing follow-up: [placeholder]"

TOOL_REGISTRY = {
    "summarize_messages": summarize_messages,
    "post_to_slack": post_to_slack,
    "detect_topic": detect_topic,
    "wait_for_more_data": wait_for_more_data,
    "flag_follow_up": flag_follow_up
}