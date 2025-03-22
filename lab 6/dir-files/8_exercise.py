import os
path = input("Enter the file path: ")
if os.path.exists(path):
    if os.access(path, os.R_OK) and os.access(path, os.W_OK):
        os.remove(path)
else:
    print(f"File '{path}' does not exist.")
