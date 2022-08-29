integerMassTable={'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
              'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}

def IzracunajMasu(peptide):
  masa=0
  for slovo in peptide:
    masa+=integerMassTable[slovo]
  return masa


def Cyclospectrum(peptide):
  dvostruki=peptide+peptide
  spektar=[0, IzracunajMasu(peptide)]
  p=len(peptide)

  for l in range(1, p):
    for k in range(0, p):
      subp=dvostruki[k:k+l]
      spektar.append(IzracunajMasu(subp))
  return sorted(spektar)


def Score(peptide, Spectrum):
  eksperimentalni=Cyclospectrum(peptide)
  score=0

  svi=set(eksperimentalni+Spectrum) #sve mase iz unije ovih skupova,bez duplikata
  for el in svi:
    score+=min(eksperimentalni.count(el), Spectrum.count(el))
  return  score
