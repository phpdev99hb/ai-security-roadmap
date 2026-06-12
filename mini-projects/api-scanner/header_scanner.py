import requests

url = input("Enter URL: ")

response = requests.get(url)

print("\nStatus Code:", response.status_code)

security_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]

print("\nSecurity Header Check\n")

for header in security_headers:

    if header in response.headers:
        print(f"✅ {header}")
    else:
        print(f"❌ Missing: {header}")
