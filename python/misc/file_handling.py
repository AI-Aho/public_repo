#! /usr/bin/python3

# > = w
# >> = a

filename = "our_first_text_file.txt"

#w rewrites the file
file_handler = open(filename, "w")

file_handler.write("Hello world, to the file from python!")
file_handler.close()


#a appends to a file
file_handler = open(filename, "a")

file_handler.write("\nThis is the second line")
file_handler.close()


#r reads file
file_reader = open(filename, "r")
print(file_reader)

#reads one line
line_from_file = file_reader.readline()
print(line_from_file)

#reads the rest of the file
file_content = file_reader.read()
print(file_content)

#opened fresh file and read it read
file_reader = open(filename, "r")
file_content = file_reader.read()
print(file_content)

#another way
open(filename, "a").write("\nThis write was one liner")


#recommended way to handle files
with open(filename) as file:
    content_of_the_file = file.read()

print("------------------")
#read line by line using with
with open(filename) as file2:
    for line in file2:
        print(line,end = "")