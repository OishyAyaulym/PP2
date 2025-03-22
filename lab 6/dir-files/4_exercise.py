file_name = "test.txt"
with open(file_name, 'r') as file:
    line_count = sum(1 for line in file)
print(f"Total number of lines in '{file_name}': {line_count}")