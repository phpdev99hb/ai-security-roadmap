import json
import requests

# 1. Define the target URL and the name of the output file
url = "https://kb.datums.ai/wp-json/wp/v2/posts"
output_filename = "datums_blog_data.json"

try:
    print(f"Connecting to {url}...")
    # 2. Send the HTTP GET request to fetch the data
    response = requests.get(url, timeout=10)

    # 3. Check the HTTP status code (200 means success)
    if response.status_code == 200:
        print("Connection successful! Parsing data...")

        # 4. Extract the structured JSON data from the response
        api_data = response.json()

        # 5. Open a local file and save the data cleanly
        with open(output_filename, "w", encoding="utf-8") as file:
            json.dump(api_data, file, indent=4)

        print(f"Success! All data has been saved to: '{output_filename}'")

    else:
        print(
            f"Failed to fetch data. Server responded with status code: {response.status_code}"
        )

except requests.exceptions.ConnectionError:
    print(
        "Error: Could not connect to the internet or the website is down."
    )

except requests.exceptions.Timeout:
    print("Error: The request took too long to respond. Try again later.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
