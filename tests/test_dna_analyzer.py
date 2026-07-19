from dna_analyzer import DNAAnalyzer

def test_analyze_sequence():
    analyzer = DNAAnalyzer()
    sequence = "ACGTACGT"
    result = analyzer.analyze_sequence(sequence)
    assert result["length"] == 8
    assert result["A"] == 2
    assert result["T"] == 2
    assert result["G"] == 2
    assert result["C"] == 2
    assert result["gc_content"] == 50.0

def test_analyze_empty_sequence():
    analyzer = DNAAnalyzer()
    sequence = ""
    result = analyzer.analyze_sequence(sequence)
    assert result["length"] == 0
    assert result["A"] == 0
    assert result["T"] == 0
    assert result["G"] == 0
    assert result["C"] == 0
    assert result["gc_content"] == 0

def test_analyze_sequence_all_gc_content():
    analyzer = DNAAnalyzer()
    sequence = "GGCCGGCC"
    result = analyzer.analyze_sequence(sequence)
    assert result["length"] == 8
    assert result["A"] == 0
    assert result["T"] == 0
    assert result["G"] == 4
    assert result["C"] == 4
    assert result["gc_content"] == 100.0

def test_analyze_sequence_no_gc_content():
    analyzer = DNAAnalyzer()
    sequence = "AATTAA"
    result = analyzer.analyze_sequence(sequence)
    assert result["length"] == 6
    assert result["A"] == 4
    assert result["T"] == 2
    assert result["G"] == 0
    assert result["C"] == 0
    assert result["gc_content"] == 0.0
