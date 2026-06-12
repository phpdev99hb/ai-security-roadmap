import re

user_counts = {}
failed_counts = {}

with open("mini-projects/log-analyzer/sample.log") as file:

    for line in file:

        user_match = re.search(r"user=(\w+)", line)

        if not user_match:
            continue

        username = user_match.group(1)

        user_counts[username] = user_counts.get(username, 0) + 1

        if "LOGIN_FAILED" in line:

            failed_counts[username] = failed_counts.get(username, 0) + 1

print("\n=== User Activity ===")

for user, count in user_counts.items():
    print(f"{user}: {count} events")

print("\n=== Suspicious Users ===")

for user, count in failed_counts.items():

    if count >= 3:
        print(f"⚠️ Possible brute force attack on {user}")
