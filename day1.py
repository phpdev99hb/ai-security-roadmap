name = "Bro"
age = 14

print(name)
print(age)

if age >= 18:
    print("Adult")
else:
    print("You are not adult")

for i in range(5):
    print(i)

def greet(name):
    print(f"Hello {name}")

greet("tushar")

users = ["admin", "guest"]

print(users)

user = {
    "name": "Divyanshu",
    "role": "admin"
}

print(user["name"])


with open("test.txt", "w") as f:
    f.write("Hello")

# print("Test")

with open("test.txt") as f:
    print(f.read())

print("Test")