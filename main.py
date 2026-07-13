
from file_handler import FileHandler
from validator import Validator

try:                    
    file_handler = FileHandler()
    validator = Validator()
    file_name = input("Enter DNA sequence file name with extension: ")
    data = file_handler.read_file(file_name)
    is_valid, message = validator.validate_sequence(data)
    print(is_valid,message)                         
except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An error occurred while reading the file. {e}")