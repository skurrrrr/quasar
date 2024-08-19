#!/bin/bash

#make it executable
chmod +x /usr/local/bin/quasar/quasar.py

read -p "What shall we call this machine?: " this_machine

# Create the quasar_config.json file in /usr/local/bin/quasar
echo "{\"this machine\": \"$this_machine\", \"API\": \"milfrogs.com\"}" > /usr/local/bin/quasar/quasar_config.json > /usr/local/bin/quasar/quasar_config.json

# Give the file read permission to everyone
chmod 755 /usr/local/bin/quasar/quasar_config.json

# Add cron job
(sudo crontab -l; echo "@reboot sudo python3 /usr/local/bin/quasar/reboot.py") | crontab -