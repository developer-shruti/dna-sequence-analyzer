from validator import Validator

# Valid sequence
def test_valid_sequence():
    validator_test = Validator()
    sequence = "ACGTACGT"
    is_valid, message = validator_test.validate_sequence(sequence)
    assert is_valid is True
    assert message == "The sequence is valid."

# Invalid sequence
def test_invalid_sequence():
    validator_test = Validator()
    sequence = "ACGTACGTN"
    is_valid, message = validator_test.validate_sequence(sequence)
    assert is_valid is False
    assert message == "The sequence is invalid. The nucleotide 'N' at position 9 is not valid."

# Empty sequence
def test_empty_sequence():
    validator_test = Validator()
    sequence = ""
    is_valid, message = validator_test.validate_sequence(sequence)
    assert is_valid is False
    assert message == "The sequence is empty."