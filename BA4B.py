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
  
  
  def ReverseComplement(dna):
  rc=""
  for i in range(0, len(dna)):
    if dna[i]=="A":
      rc+="T"
    elif dna[i]=="C":
      rc+="G"
    elif dna[i]=="G":
      rc+="C"
    elif dna[i]=="T":
      rc+="A"
  rc=rc[::-1]
  return rc


def DnaToRna(dna):
  rna=""
  for i in range(0, len(dna)):
    if dna[i]=="T":
      rna+="U"
    else:
      rna+=dna[i]
  return rna


def ProteinTranslation(rna): #prevodi rna u niz aminokiselina
  peptide=[]
  kodoni=get_genetic_code_codons() #dict
  for i in range(0, len(rna), 3):
    slovo=kodoni[rna[i:i+3]]
    if slovo=="*":
      break
    peptide.append(slovo)
  rj="".join(peptide)
  return rj


def PeptideEncoding(dna, peptide):
  podstringovi=[]
  p=len(peptide) #komad dna koji kodira taj peptid je onda dug 3*p
  for i in range(0, len(dna)-(3*p)-1):
    isjecak=dna[i:i+(3*p)]
    isjecak_rc=ReverseComplement(dna[i:i+(3*p)])
    rna=DnaToRna(isjecak)
    rna_rc=DnaToRna(isjecak_rc)
    if (ProteinTranslation(rna)==peptide or ProteinTranslation(rna_rc)==peptide):
      podstringovi.append(isjecak)
  for rj in podstringovi:
    print (rj)
