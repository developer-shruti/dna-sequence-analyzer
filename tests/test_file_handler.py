from file_handler import FileHandler

def test_read_fasta_file():
    handler = FileHandler()
    sequence = handler.read_file("sample_fasta.fasta")
    assert sequence == ">sequence_001\nATGCGTACGTAGCTAG"