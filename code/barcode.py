import numpy as np

def random_dna_sequence(length:int) -> str:
    return ''.join(np.random.choice(('A', 'C', 'T', 'G')) for _ in range(length))

def barcode()-> str:
    return random_dna_sequence(21) + 'TAGGGATAACAGGGTAAT' + random_dna_sequence(21)


