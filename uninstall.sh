#!/bin/bash


# deletes stuff
rm -rf /usr/local/bin/quasar/

# removes cron job (NEEDS TO BE FIXED)
#sudo sed -i '/.*python3 \/usr\/local\/bin\/quasar\.py/d' /tmp/$(crontab  -l)