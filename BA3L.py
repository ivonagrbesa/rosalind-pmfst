def ReconstructStringGappedPatterns(k, d, parovi):
  FirstPatterns=[]
  SecondPatterns=[]
  for i in range(len(parovi)):
    FirstPatterns.append(parovi[i][0])
    SecondPatterns.append(parovi[i][1])
  
  PrefixString=FirstPatterns[0]
  SuffixString=SecondPatterns[0]

  for i in range(1, len(FirstPatterns)):
    PrefixString+=FirstPatterns[i][-1] #od svih ostalih prvih kmera dodajemo samo po zadnje slovo
  for i in range(1, len(SecondPatterns)):
    SuffixString+=SecondPatterns[i][-1]
  
  #prefixstring i suffixstring trebali bi se preklopiti od k+d+1 indeksa do kraja prefixstring
  #provjeravamo ima li na tom dijelu razlikovanja
  for i in range(k+d+1, len(PrefixString)):
    if PrefixString[i]!=SuffixString[i-k-d]:
      return "Ne postoji takav string"
  
  return PrefixString+SuffixString[len(SuffixString)-k-d:]
