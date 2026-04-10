

def predict_protein_mass(sequence):
  
    residue_masses = {
        "G": 57.02,
        "A": 71.04,
        "S": 87.03,
        "P": 97.05,
        "V": 99.07,
        "T": 101.05,
        "C": 103.01,
        "I": 113.08,
        "L": 113.08,
        "N": 114.04,
        "D": 115.03,
        "Q": 128.06,
        "K": 128.09,
        "E": 129.04,
        "M": 131.04,
        "H": 137.06,
        "F": 147.07,
        "R": 156.10,
        "Y": 163.06,
        "W": 186.08
    }

    total_mass = 0.0
    sequence = sequence.upper()

    for amino_acid in sequence:
        if amino_acid not in residue_masses:
            raise ValueError(f"Error: amino acid '{amino_acid}' has no recorded mass.")
        total_mass += residue_masses[amino_acid]

    return total_mass

example_sequence = "GAST"
print("Protein sequence:", example_sequence)
print("Protein mass:", predict_protein_mass(example_sequence), "amu")


