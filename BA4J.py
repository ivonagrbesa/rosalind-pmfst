integerMassTable={'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
              'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}


def IzracunajMasu(peptide):
  masa=0
  slova=list(peptide) #od stringa napravimo listu
  for s in slova:
    masa+=integerMassTable[s]
  return masa


def LinearSpectrum(peptide):
  spektar=[0] #prazni peptid (triv.)

  for i in range(1, len(peptide)): #netrivijalni podstringovi
    for j in range(0, len(peptide)):
      if j+i<=len(peptide):
        m=IzracunajMasu(peptide[j:j+i])
        spektar.append(m)
  
  spektar.append(IzracunajMasu(peptide)) #cijeli string  (triv.)
  spektar.sort() #uzlazno
  return spektar


