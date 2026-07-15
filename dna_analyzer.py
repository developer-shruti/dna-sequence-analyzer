class DNAAnalyzer:
    def analyze_sequence(self, sequence: str) -> dict:
        if sequence is None or sequence.strip() == "":
            return {
                        "length": 0,
                        "A": 0,
                        "T": 0,
                        "G": 0,
                        "C": 0,
                        "gc_content": 0
                }
        else:
            sequence = sequence.upper()
            g_count = sequence.count("G")
            c_count = sequence.count("C")
            return {
                "length": len(sequence),
                "A": sequence.count("A"),
                "T": sequence.count("T"),
                "G": g_count,
                "C": c_count,
                "gc_content": (g_count + c_count) / len(sequence) * 100
            }