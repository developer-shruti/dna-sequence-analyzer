class FileHandler:

    def read_file(self, file_name: str) -> str:
        
        file_path = "data/" + file_name
        with open(file_path, "r") as file:
            return file.read()
             
    
    
    