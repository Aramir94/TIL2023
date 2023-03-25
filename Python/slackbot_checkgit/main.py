import os
import datetime
import requests
import sqlite3

# Define the Slack webhook URL and users to check
webhook_url = "https://hooks.slack.com/services/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"
users = ["Aramir94", "raunee", "LearningnRunning"]

# Define the amount of fine for not committing code (in dollars)
fine_amount = 3000

# Get the current date
today = datetime.date.today()

# Initialize the SQLite connection
conn = sqlite3.connect("fines.db")
cursor = conn.cursor()

# Create the fines table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS fines (user TEXT, date TEXT, fine INTEGER)")

# Define the message text and total fine amount
message = ""
fine_total = 0

# Iterate over the users and check their commit counts
for user in users:
    # Define the GitHub API endpoint URL for the user's activity
    url = f"https://api.github.com/users/{user}/events"
    
    # Make a request to the GitHub API
    response = requests.get(url)
    
    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        events = response.json()
        
        # Count the user's commits for today
        commit_count = 0
        for event in events:
            if event["type"] == "PushEvent" and event["created_at"].startswith(str(today)):
                commit_count += len(event["payload"]["commits"])
        
        # Add the user's commit count to the message
        message += f"{user}: {commit_count} commits today\n"
        
        # If the user hasn't committed code today, add a fine to the database and the total fine amount
        if commit_count == 0:
            cursor.execute("INSERT INTO fines (user, date, fine) VALUES (?, ?, ?)", (user, str(today), fine_amount))
            conn.commit()
            message += f"{user}: {fine_amount}원 벌금 확정입니다!! \n"
    else:
        message += f"Error checking {user}'s activity\n"

# Add the total fine amount to the message

# Send the message to the Slack webhook URL
response = requests.post(webhook_url, json={"text": message})
if response.status_code == 200:
    print("Message sent to Slack")
else:
    print(f"Error sending message to Slack ({response.status_code}): {response.text}")
