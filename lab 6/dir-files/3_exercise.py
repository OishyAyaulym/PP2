import os
path = input("Enter the path: ")
if os.path.exists(path):
    print(f"The path '{path}' exists.")
    print(f"Directory: {os.path.dirname(path)}")
    print(f"Filename: {os.path.basename(path)}")
else:
    print(f"The path '{path}' does not exist.")