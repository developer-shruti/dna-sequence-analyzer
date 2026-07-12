
from file_handler import FileHandler

try:                    
    file_handler = FileHandler()
    file_name = input("Enter DNA sequence file name with extension: ")
    data = file_handler.read_file(file_name)
    print(data)                         
except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An error occurred while reading the file. {e}")