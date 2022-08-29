def TheoreticalSpectrum(peptide):
  #zbroji masu po svakom slovu
  spektar=[0, sum(peptide)]
  dvostruki=peptide+peptide
  p=len(peptide)

  for l in range(1, p):
    for k in range(0, p):
      podpeptid=dvostruki[k:k+l]
      spektar.append(sum(podpeptid))
  return sorted(spektar)

# peptide je niz integera, ima ih isto koliko i slova (ista indeksacija)
def Expand(peptides):
  mase=[57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
  novi_peptidi=[]
  for peptide in peptides:
    for masa in mase:
      novi_peptidi.append(peptide+[masa])
  return novi_peptidi

# peptide je linearan
def IsConsistent(peptide, Spectrum):
  linearni_spektar=[0, sum(peptide)]
  for l in range(1, len(peptide)):
    for k in range(0, len(peptide)-l+1):
      subpeptide=peptide[k:k+l]
      linearni_spektar.append(sum(subpeptide))
  
  rj=[]
  for el in linearni_spektar:
    if el in Spectrum:
      rj.append(True)
    else:
      rj.append(False)
  return rj


def CyclopeptideSequencing(Spectrum):
  Peptides=[[]]
  rj=[]
  while len(Peptides)>0:
    Peptides=Expand(Peptides)
    for peptide in Peptides:
      if sum(peptide)==Spectrum[-1]:
        if TheoreticalSpectrum(peptide)==Spectrum:
          rj.append(peptide)
        Peptides=[p for p in Peptides if p!=peptide] #ovo je isto ka da smo izbacili peptide
      elif False in IsConsistent(peptide, Spectrum):
        Peptides=[p for p in Peptides if p!=peptide]
  return rj
