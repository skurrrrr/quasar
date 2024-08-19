import requests
import json
import subprocess

# Load the JSON file
with open('/usr/local/bin/quasar/quasar_config.json') as f:
    config = json.load(f)

# Get public IP address using curl command
public_ip = subprocess.check_output(['curl', 'http://api.ipify.org']).decode().strip()

# Check if public IP is different from the one in the JSON file
if public_ip != config['IP']:
    # Update the JSON file with the new public IP
    config['IP'] = public_ip

    # Convert dictionary back to JSON string
    json_string = json.dumps(config)

    # Save changes to the JSON file
    with open('/usr/local/bin/quasar/quasar_config.json', 'w') as f:
        f.write(json_string)

    # Create the webhook data
    webhook_url = 'https://discord.com/api/webhooks/1275206757173432352/8KFB-HjXDjPxhQ8RDAIcXGqJ13gc7F8_7p9vitIpVn-IA8m3_ZEiJxZo2kyVgvWygpzW'
    data = {
        "username": config['this machine'],
        "content": f"IP Address changed to {public_ip}"
    }
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the POST request
    response = requests.post(webhook_url, json=data, headers=headers)

    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Error: {response.text}")
else:
    print("IP Address is already correct.")