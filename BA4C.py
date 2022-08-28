def get_amino_acid_mass():
    mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }

    return mass
  
  
  def IzracunajMasu(peptide):
    masa=0
    D=get_amino_acid_mass()
    slova=list(peptide)
    for s in slova:
      masa+=D[s] #za svaki key (slovo) dohvatimo value(masu)
    return masa

def TheoreticalSpectrum(peptide):
  rj=[0, IzracunajMasu(peptide)] #0 i uk.masa
  p=len(peptide)
  dvostruki=peptide+peptide #zato sta trazimo podstringove ciklickog peptida
  for k in range(1, p): #sve manje duljine
    for l in range(0, p): #sve pozicije s kojih ih mozemo  izrezivati
      subpeptide=dvostruki[l:l+k]
      rj.append(IzracunajMasu(subpeptide))
  return rj

