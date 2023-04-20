import os
import datetime
import requests
import sqlite3

# Define the Slack webhook URL and users to check
webhook_url = os.environ["SLACK_WEBHOOK_URL"]

message = f"깃 커밋 체크 한시간 전 준비 바랍니다 \n\n\n"
# Add the total fine amount to the message

# Send the message to the Slack webhook URL
response = requests.post(webhook_url, json={"text": message})
if response.status_code == 200:
    print("Message sent to Slack")
else:
    print(f"Error sending message to Slack ({response.status_code}): {response.text}")
    response = requests.post(webhook_url, json={"text": "webhook url something wrong"})
