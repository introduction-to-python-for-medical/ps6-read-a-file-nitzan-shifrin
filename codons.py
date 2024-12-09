def create_codon_dict(file_path):
    mapping_codons_amino = {}
    with open(file_path, "r") as file:
        rows = file.readlines()

    for row in rows:
        row = row.strip()
        cells = row.split('\t')

        codons = cells[0]
        amino_acids = cells[2]

        mapping_codons_amino[codons] = amino_acids

    return mapping_codons_amino


