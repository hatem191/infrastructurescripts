# How to Automate Incident Response with Slack Notifications
import requests

def send_slack_notification(channel, message):
    webhook_url = "https://hooks.slack.com/services/your/webhook/url"
    payload = {
        "channel": channel,
        "text": message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification: {response.status_code}")

# Example usage
send_slack_notification("#incident-response", "Critical security incident detected! Immediate action required.")
