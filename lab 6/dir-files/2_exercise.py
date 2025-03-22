import os
path = os.getcwd()
print(f"Path accessibility: Exists: {os.access(path, mode=os.EX_OK)}, Readable: {os.access(path, mode=os.R_OK)}, Writable: {os.access(path, mode=os.W_OK)}, Executable: {os.access(path, mode=os.X_OK)}")