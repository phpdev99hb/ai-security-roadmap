import re

# Initialize counters and an empty set to track unique users who logged in
failed = 0
success = 0
successful_users = set()

# Open and process the log file line by line (more memory efficient)
with open("mini-projects/log-analyzer/sample.log", "r") as file:
    for line in file:
        if "LOGIN_FAILED" in line:
            failed += 1

        if "LOGIN_SUCCESS" in line:
            success += 1
            # Extract and store the username for successful logins
            user_match = re.search(r"user=(\w+)", line)
            if user_match:
                successful_users.add(user_match.group(1))

# Print the final summary results
print(f"Successful Logins: {success}")
print(f"Failed Logins: {failed}")
print("Users who successfully logged in:")
for user in sorted(successful_users):
    print(f"- {user}")
