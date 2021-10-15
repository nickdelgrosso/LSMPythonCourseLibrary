
def dna_nucleotide_frequency(seq):
    """
    A function to count freq of nucleotides in a sequence

    :param seq: A sequence of DNA string
    :return: a dictionary with AGTC freq count

    >>> dna_nucleotide_frequency('AGTCG')
    {'A': 1, 'G': 2, 'T': 1, 'C': 1}

    >>> dna_nucleotide_frequency('AGTCTACG')
    {'A': 2, 'G': 2, 'T': 2, 'C': 2}
    """

    A = seq.count('A')
    G = seq.count('G')
    T = seq.count('T')
    C = seq.count('C')
    return {'A': A, 'G': G, 'T': T, 'C': C}
