file = open("notes.txt", "w")
file.write("This is my first saved note.\n")
file.write("Python can read and write files.\n")
file.close()

print("File written successfully")

file = open("notes.txt", "r")
contents = file.read()
file.close()

print("Here is what the file contains:")
print(contents)

file = open("notes.txt", "a")
file.write("This line was added later.\n")
file.close()

file=open("notes.txt","r")
print(file.read())
file.close()
