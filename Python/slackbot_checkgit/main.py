import os
import datetime
import requests
import sqlite3

# Define the Slack webhook URL and users to check
# webhook_url =  os.environ['SLACK_WEBHOOK_URL']
webhook_url = "https://hooks.slack.com/services/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"
users = ["Aramir94", "raunee", "LearningnRunning"]

# Define the amount of fine for not committing code (in dollars)
fine_amount = 3000

# Get the current date
today = datetime.date.today()

# Initialize the SQLite connection
conn = sqlite3.connect("fines.db")
cursor = conn.cursor()

conn_commits = sqlite3.connect("commits.db")
cursor_commits = conn_commits.cursor()

# Create the fines table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS fines (user TEXT, date TEXT, fine INTEGER)")

# Create the commits table if it doesn't exist
cursor_commits.execute("CREATE TABLE IF NOT EXISTS commits (user TEXT, date TEXT, count INTEGER)")
# Define the message text and total fine amount
message = f"\n{today.strftime('%Y-%m-%d')}일 대탈출 멤버들 깃 확인 보고 \n\n\n"
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
        message += f"{user}: {commit_count} commits today\n\n"

        # If the user hasn't committed code today, add a fine to the database and the total fine amount
        if commit_count == 0:
            cursor.execute("INSERT INTO fines (user, date, fine) VALUES (?, ?, ?)", (user, str(today), fine_amount))
            conn.commit()

            saying_url = "https://api.quotable.io/random"
            saying_response = requests.get(saying_url)
            if saying_response.status_code == 200:
                saying = saying_response.json()["content"]
                author = saying_response.json()["author"] 
                text =  f"{saying}\n- {author}\n\n"
            else:
                text = f"Let's work hard and find joy in our coding tomorrow!!\n\n"
            
            message += f"{user}: {fine_amount}원 벌금 확정입니다!! \n {text}"
            # Add a message attachment with the user's name and a message encouraging hard work and joy
        else:
             cursor.execute("INSERT INTO fines (user, date, fine) VALUES (?, ?, ?)", (user, str(today), 0))

        # Store the user's commit count in the database
        cursor_commits.execute("INSERT INTO commits (user, date, count) VALUES (?, ?, ?)", (user, str(today), commit_count))
        conn_commits.commit()
    else:
        message += f"Error checking {user}'s activity\n\n"

# Add the total fine amount to the message

# Send the message to the Slack webhook URL
response = requests.post(webhook_url, json={"text": message})
if response.status_code == 200:
    print("Message sent to Slack")
else:
    print(f"Error sending message to Slack ({response.status_code}): {response.text}")
    webhook_url = "https://hooks.slack.com/services/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"
    response = requests.post(webhook_url, json={"text": "webhook url something wrong"})
