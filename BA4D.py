mase=[57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
# integer mase svih aminokiselina


def CountingPeptides(m):
  D=dict()
  # ne postoje peptidi s masom manjom od 57
  for i in range(0, 57):
    D[i]=0

  #promatramo peptide s masama od najmanje(57) do unesene (m)
  for masa in range(57, m+1):
    D[masa]=mase.count(masa) #koliko se puta masa pojavila u nizu (ove od 57 do 186 ce tu imat 1 pojavljivanje)
    for broj in mase:
      if masa>=broj:
        if D[masa-broj]>0:
          D[masa]+=D[masa-broj]
  return D[masa]
