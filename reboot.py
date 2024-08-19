import requests

webhook_url = 'https://discord.com/api/webhooks/1275206757173432352/8KFB-HjXDjPxhQ8RDAIcXGqJ13gc7F8_7p9vitIpVn-IA8m3_ZEiJxZo2kyVgvWyg'

data = {
    "username": "wirelessdan.net/172.232.170.248",
    "content": "system reboot complete"
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(webhook_url, json=data, headers=headers)

if response.status_code == 204:
    print("Message sent successfully!")
else:
    print(f"Error: {response.text}")