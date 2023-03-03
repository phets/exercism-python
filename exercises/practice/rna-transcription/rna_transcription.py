"""
Module to translate strands of DNA to RNA.
"""

# Dictionary holding the nucleotide complements.
translation = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}


def to_rna(dna_strand: str) -> str:
    """
    Translates a strand of DNA into the complementary strand of RNA.

    Args:
        dna_strand (str): String representing a DNA strand. e.g. "CGAT"

    Returns:
        str: String representing the RNA strand. e.g. "GCUA"
    """
    return ''.join(translation[base] for base in dna_strand)


