from report_generator import ReportGenerator

def test_generate_report():
    report_generator = ReportGenerator()
    sequence = {
                    "length": 8,
                    "A": 2,
                    "T": 2,
                    "G": 2,
                    "C": 2,
                    "gc_content": 50.0
                }
    result = report_generator.generate_report(sequence)
    assert "DNA Analysis Report" in result
    assert "Sequence Length : 8" in result
    assert "Adenine Count     : 2" in result
    assert "Thymine Count     : 2" in result
    assert "Cytosine Count    : 2" in result
    assert "Guanine Count     : 2" in result
    assert "GC Content (%)    : 50.00" in result
    assert "Nucleotide Counts" in result
