
from file_handler import FileHandler
from validator import Validator
from dna_analyzer import DNAAnalyzer
from report_generator import ReportGenerator

try:                    
    file_handler = FileHandler()
    validator = Validator()
    dna_analyzer = DNAAnalyzer()
    file_name = input("Enter DNA sequence file name with extension: ")
    data = file_handler.read_file(file_name)
    is_valid, message = validator.validate_sequence(data)
    if is_valid:
        analyzed_results=dna_analyzer.analyze_sequence(data)
        report_generator = ReportGenerator()
        report = report_generator.generate_report(analyzed_results)
        print(report)
    else:
        print(message)                         
except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An error occurred while reading the file. {e}")