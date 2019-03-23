def proteins(strand):
    proteins = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        if codon in codons.keys() and codons[codon] != "STOP":
            proteins.append(codons[codon])

        else:
            return proteins

    return proteins





codons = {"AUG" : "Methionine", "UUU" : "Phenylalanine", "UUC" : "Phenylalanine", "UUA" : "Leucine",
        "UUG" : "Leucine", "UCU" : "Serine", "UCC" : "Serine", "UCA" : "Serine", "UCG" : "Serine",
        "UAU" : "Tyrosine", "UAC" : "Tyrosine", "UGU" : "Cysteine" , "UGC" : "Cysteine", "UGG" : "Tryptophan",
        "UAA" : "STOP", "UAG" : "STOP", "UGA" :  "STOP"}
