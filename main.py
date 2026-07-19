from file_handler import FileHandler
from validator import Validator
from dna_analyzer import DNAAnalyzer
from report_generator import ReportGenerator
from logger_config import logger

try:                    
    file_handler = FileHandler()
    validator = Validator()
    dna_analyzer = DNAAnalyzer()
    logger.info("Application started")
    file_name = input("Enter DNA sequence file name with extension: ")
    logger.info(f"File to be read is {file_name}")
    data = file_handler.read_file(file_name)
    is_valid, message = validator.validate_sequence(data)
    if is_valid:
        logger.info("The sequence is valid.")
        analyzed_results=dna_analyzer.analyze_sequence(data)
        report_generator = ReportGenerator()
        report = report_generator.generate_report(analyzed_results)
        print(report)
        logger.info(f"Report generated successfully for file: {file_name}")
    else:
        logger.warning(f"The sequence is invalid. {message}")
        print(message)                         
except FileNotFoundError:
    logger.exception("The file was not found.")
    print("Error: The file was not found.")
except Exception as e:
    logger.exception(f"An error occurred while reading the file. {e}")
    print(f"An error occurred while reading the file. {e}")
finally:
    logger.info("Application finished")