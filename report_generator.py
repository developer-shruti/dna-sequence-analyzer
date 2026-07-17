class ReportGenerator:
    def generate_report(self, analyzed_dna_sequence: dict) -> str:
        final_report=f""
        title_divider = "==================================================="
        title_label = "DNA Analysis Report"
        subtitle_divider = "---------------------------------------"
        sequence_report = f"Sequence Length : {analyzed_dna_sequence['length']}"
        subtitle_label = "Nucleotide Counts"
        gccontent_report = f"GC Content (%)    : {analyzed_dna_sequence['gc_content']:.2f}"
        acount_report = f"Adenine Count     : {analyzed_dna_sequence['A']}"
        tcount_report = f"Thymine Count     : {analyzed_dna_sequence['T']}"
        ccount_report = f"Cytosine Count    : {analyzed_dna_sequence['C']}"
        gcount_report = f"Guanine Count     : {analyzed_dna_sequence['G']}"

        final_report = f"{title_divider}\n\n{title_label}\n\n{title_divider}\n\n{sequence_report}\n\n{subtitle_label}\n{subtitle_divider}\n{acount_report}\n{tcount_report}\n{ccount_report}\n{gcount_report}\n{gccontent_report}\n{title_divider}"

        return final_report