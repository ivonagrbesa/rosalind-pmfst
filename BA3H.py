def StringReconstruction(k, patterns):
  prefiksi=[]
  sufiksi=[]
  D=dict() #itemsi su (prefiks, njegovo zadnje slovo)

  for kmer in patterns:
    prefiksi.append(kmer[:-1])
    sufiksi.append(kmer[1:])
    D[kmer[:-1]]=kmer[-1]    #D[prefiks]=njegovo zadnje slovo

  for p in prefiksi:
    if p not in sufiksi:
      pocetak=p
  
  for s in sufiksi:
    if s not in prefiksi:
      kraj=s
  
  tekst=pocetak+D[pocetak]
  

  while True:
    ostatak=tekst[len(tekst)-k+1:len(tekst)]
    if ostatak==kraj:
      break
    else: #ako nije kraj, onda on ima svoje zadnje slovo u dictionaryju
      tekst=tekst+D[ostatak]
  return tekst
