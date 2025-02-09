import os
import subprocess

try:
    uptime = os.sysconf('uptime')
    hours, minutes, seconds = divmod(uptime, 3600)
    hours %= 60
    minutes, seconds = divmod(minutes, 60)
except OSError as e:
    print(f"Error getting uptime: {e}")
    exit()

hostname = os.hostname()

try:
    result = subprocess.run(['w'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error getting current users")
        exit()
    output = result.stdout
    lines = output.split('\n')
    # Count each non-empty line to determine the number of users
    current_users_count = sum(1 for line in lines if line.strip())
except Exception as e:
    print(f"Error: {e}")
    exit()

print(f"Uptime: {hours:.2f}:{minutes:02d}:{seconds:02d}")
print("Hostname:", hostname)
print(f"Current Users: {current_users_count}")