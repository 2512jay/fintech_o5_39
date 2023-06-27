# Read from a file
with open("input.txt", "r") as file:
    contents = file.read()
    print(contents)

# Write to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!")
