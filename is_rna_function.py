def is_rna(seq):
    """
    This function will tell you whether your sequence is RNA or not
    :param seq: seq is any DNA / RNA sequence
    :return: True if it is RNA, False if it is DNA, False if none of U / T are in the sequence

    >>> is_rna("AUCG")
    True
    >>> is_rna("ATCG")
    False
    >>> is_rna("ACCG")
    'NA'
    >>> is_rna("ATUCG")
    'NA'
    """
    seq = seq.upper()
    uracile = "U"
    thymine = "T"
    if uracile in seq and thymine not in seq:
        return(True)
    elif thymine in seq and uracile not in seq:
        return(False)
    else:
        return("NA")


import doctest
doctest.testmod(verbose=True)