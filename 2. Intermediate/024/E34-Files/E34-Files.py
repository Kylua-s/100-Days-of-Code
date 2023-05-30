# Exercise 34 - Files

# Opens "my-file.txt" and needs close function
file = open("my_file.txt")
content = file.read()
print(content)
file.close()

# Opens "my-file.txt" different
with open("my_file.txt") as file:
    content = file.read()
    print(content)
