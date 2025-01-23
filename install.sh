#!/bin/bash

# Make it executable
chmod +x /usr/local/bin/quasar/check_ip.py /usr/local/bin/quasar/reboot.py

read -p "What shall we call this machine?: " this_machine

read -p "Webhook for this machine (should not be exposed to the public): " webhook

# Get public IP address using curl command
public_ip=$(curl -4 http://icanhazip.com)

# Create the quasar_ config.json file in /usr/local/bin/quasar
echo "{\"this machine\": \"$this_machine\", \"webhook\": \"$webhook\", \"API\": \"milfrogs.com\", \"IP\": \"$public_ip\"}" > /usr/local/bin/quasar/quasar_config.json

# Give the file read permission to everyone
chmod 755 /usr/local/bin/quasar/quasar_config.json

# Add cron jobs
(sudo crontab -l; echo "@reboot sudo python3 /usr/local/bin/quasar/reboot.py") | crontab -
(sudo crontab -l; echo "*/1 * * * * sudo python3 /usr/local/bin/quasar/check_ip.py") | crontab -