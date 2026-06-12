import re

failed_users = {}

with open("mini-projects/log-analyzer/sample.log") as file:
    logs = file.readlines()

for line in logs:

    if "LOGIN_FAILED" in line:

        user = re.search(r"user=(\w+)", line)

        if user:

            username = user.group(1)

            failed_users[username] = failed_users.get(username, 0) + 1

print("\nSuspicious Accounts:")

for user, count in failed_users.items():

    if count >= 3:
        print(f"WARNING: {user} has {count} failed logins")
