__author__ = 'Mace'

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    count = 0

    for char in dna:
        count = count + 1

    return count


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    longer = False

    if get_length(dna1) > get_length(dna2):
        longer = True

    return longer


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    count = 0

    for char in dna:
        if nucleotide == char:
            count = count + 1

    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    contains = False

    if dna2 in dna1:
        contains = True

    return contains


def is_valid_sequence(seq):
    ''' (str) -> bool

    Return True if the str parameter only contains the characters
    'A', 'T', 'C', or 'G'

    >>> is_valid_sequence('AGTCGA')
    True
    >>> is_valid_sequence('NOTAGTRUE')
    False
    '''

    valid = True

    for char in seq:
        if char != 'A' and char != 'G' and char != 'T' and char != 'C':
            valid = False

    return valid

def insert_sequence(dna1, dna2, index):
    ''' (str, str, int) -> str

    Return the string of containing the second string inserted into
    the first string and the indicated index

    >>> insert_sequence('AAGG', 'TT', 2)
    'AATTGG'
    >>> insert_sequence('ATGCGA', 'A', 0)
    'AATGCGA'
    '''

    inserted = ''

    inserted = dna1[0:index] + dna2 + dna1[index:]

    return inserted


def get_complement(nucleotide):
    ''' (str) -> str

    Return the complement of the nucleotide parameter

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    >>> get_complement('C')
    'G'
    '''

    complement = ''

    if nucleotide == 'A':
        complement = 'T'
    elif nucleotide == 'T':
        complement = 'A'
    elif nucleotide == 'G':
        complement = 'C'
    elif nucleotide == 'C':
        complement = 'G'

    return complement


def get_complementary_sequence(dna):
    ''' (str) -> str

    Return complementary sequence of dna of dna parameter

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('GC')
    'CG'
    '''

    compSequence = ''

    for char in dna:
        compSequence = compSequence + get_complement(char)

    return compSequence
