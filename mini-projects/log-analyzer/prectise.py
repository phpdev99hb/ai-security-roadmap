import re

# Use a dictionary to keep track of event counts for each user
user_counts = {}

# Open and process the log file line by line
with open("mini-projects/log-analyzer/sample.log", "r") as file:
    for line in file:
        # Check if the line contains a login attempt (Success or Failed)
        if "LOGIN_SUCCESS" in line or "LOGIN_FAILED" in line:
            # Extract the username using regex
            user_match = re.search(r"user=(\w+)", line)

            if user_match:
                username = user_match.group(1)

                # If the user is already in our dictionary, add 1 to their count
                # If they are new, start their count at 1
                if username in user_counts:
                    user_counts[username] += 1
                else:
                    user_counts[username] = 1

# Print the total number of unique users (the number of keys in our dictionary)
print(f"Total Users: {len(user_counts)}\n")

# Print the event breakdown for each user
for user, count in user_counts.items():
    # Simple grammar fix: use "event" for 1, and "events" for 2 or more
    event_word = "event" if count == 1 else "events"
    print(f"{user} = {count} {event_word}")
