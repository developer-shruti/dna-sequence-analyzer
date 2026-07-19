import logging
from logger_config import logger

class Validator:
    def validate_sequence(self, sequence: str) -> tuple:
        if sequence is None or sequence.strip() == "":
            logger.warning("The sequence is empty.")
            return (False, "The sequence is empty.")
        else:
            valid_set = {"A", "C", "G", "T"}
            default_message = (True, "The sequence is valid.")
            for index, nucleotide in enumerate(sequence.upper()):
                if nucleotide in valid_set:
                    continue
                else:
                    default_message = (False, f"The sequence is invalid. The nucleotide '{nucleotide}' at position {index+1} is not valid.")
                    break
            return default_message
