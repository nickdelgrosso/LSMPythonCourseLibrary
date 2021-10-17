def get_codon_at(seq, idx):
    """
    Gets codon at a position 'idx'
    :param seq: A string of nucleotides
    :param idx: A position in 'int' at which the nucleotide is to be printed
    :return: A nucleotide at position 'idx'

    >>> get_codon_at('AGTCCTCGCAT', 3)
    'T'
    >>> get_codon_at('GCTAGCTGACTAA', 45)
    The length of sequence is only 12 not 45
    """
    if idx-1 > len(seq):
        print('The length of sequence is only ' + str(len(seq)-1) + ' not ' + str(idx))
    else:
        return seq[idx-1]
