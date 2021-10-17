def is_DNA(seq):
    """
    Checks if the given sequence is DNA

    :param seq: string, input sequence
    :return: True if the given sequence is DNA,
    False if the given sequence is RNA, 'not sure'
    if the given sequence consists of G, C, and A

    >>> is_DNA("ATCG")
    True

    >>> is_DNA("GUACGU")
    False
    """

    if 'T' in seq:
        return True
    elif 'U' in seq:
        return False
    else:
        return 'not sure'

import doctest

doctest.testmod(verbose = True)

