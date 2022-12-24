from Bio.Data import CodonTable

codon_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
print(codon_table)
