import os
# listdir() functions returns the contents of a directory as a list of strings which each string is the file or subdirectory name.
# it takes the path as a parameter
contents = os.listdir(".")
print(contents)