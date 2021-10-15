def standardise_uppercase(seq):
    """
    Return a sequence with uppercase letters from the given sequence as a string.
    :param seqs: A sequnece as a string with upper or lower case letters.
    :return: An output sequence as a string with all letters are uppercased.

    Examples

    >>> standardise_uppercase(aauCcG)
    'AAUCCG'

    >>> standardise_uppercase(aucgaucg)
    'AUCGAUCG'
    """
    seq_upper = seq.upper()
    return seq_upper


import doctest
doctest.testmod()

