import requests
import json

# Load the JSON file
with open('/usr/local/bin/quasar/quasar_config.json') as f:
    config = json.load(f)

# Update the webhook data
webhook_url  = 'https://discord.com/api/webhooks/1275206757173432352/8KFB-HjXDjPxhQ8RDAIcXGqJ13gc7F8_7p9vitIpVn-IA8m3_ZEiJxZo2kyVgvWygpzW'
data  = {
     "username": config['this machine'],
     "content": "system reboot complete"
}

headers  = {
     'Content-Type': 'application/json'
}

response  = requests.post(webhook_url, json=data, headers=headers)

if response.status_code == 204:
    print("Message sent successfully!")
else:
    print(f"Error: {response.text}")