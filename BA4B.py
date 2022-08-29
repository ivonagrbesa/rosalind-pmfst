def get_genetic_code_codons():
    genetic_code = {
        "AAA": "K",
        "AAC": "N",
        "AAG": "K",
        "AAU": "N",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACU": "T",
        "AGA": "R",
        "AGC": "S",
        "AGG": "R",
        "AGU": "S",
        "AUA": "I",
        "AUC": "I",
        "AUG": "M",
        "AUU": "I",
        "CAA": "Q",
        "CAC": "H",
        "CAG": "Q",
        "CAU": "H",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCU": "P",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGU": "R",
        "CUA": "L",
        "CUC": "L",
        "CUG": "L",
        "CUU": "L",
        "GAA": "E",
        "GAC": "D",
        "GAG": "E",
        "GAU": "D",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCU": "A",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGU": "G",
        "GUA": "V",
        "GUC": "V",
        "GUG": "V",
        "GUU": "V",
        "UAA": "*",
        "UAC": "Y",
        "UAG": "*",
        "UAU": "Y",
        "UCA": "S",
        "UCC": "S",
        "UCG": "S",
        "UCU": "S",
        "UGA": "*",
        "UGC": "C",
        "UGG": "W",
        "UGU": "C",
        "UUA": "L",
        "UUC": "F",
        "UUG": "L",
        "UUU": "F",
    }

    return genetic_code
  
  
def RC(dna):
  rj=""
  for i in range(len(dna)):
    if dna[i]=="A":
      rj+="T"
    elif dna[i]=="C":
      rj+="G"
    elif dna[i]=="G":
      rj+="C"
    elif dna[i]=="T":
      rj+="A"
  return rj[::-1]

def Rna(dna):
  rna=""
  for slovo in dna:
    if slovo=="T":
      rna+="U"
    else:
      rna+=slovo
  return rna

def FindSubstrings(dna, peptide):
  podstringovi=[]
  p=len(peptide)
  k=3*p #podstr koji su rjesenja su duljine k

  for i in range(0, len(dna)-k+1):
    isjecak=dna[i:i+k]
    isjecak_rc=RC(isjecak)
    rna=Rna(isjecak)
    rna_rc=Rna(isjecak_rc)
    if (Translate(rna)==peptide or Translate(rna_rc)==peptide):
      podstringovi.append(isjecak)
  for p in podstringovi:
    print(p)  
