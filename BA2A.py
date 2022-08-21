def HammingDistance(s1, s2):
  d=0
  for i in range(len(s1)):
    if s1[i]!=s2[i]:
      d+=1
  return d

def dNeighbors(pattern, d, skup):
  k=len(pattern)
  sviKmeri=map(''.join, itertools.product('ACGT', repeat=k))
  for el in sviKmeri:
    if HammingDistance(el, pattern)<=d:
      skup.add(el)
      
def MotifEnumeration(dna, k, d):
  patterns=[] #za cili dna, dopustamo duplikate

  for i in range(len(dna)): 
    patterns_i=set() #za i-tu liniju, nema duplikata
    for j in range(len(dna[i])-k+1):
      susjedi=set()
      dNeighbors(dna[i][j:j+k], d, susjedi) #svi d-susjedi j-tog stringa u i-toj liniji
      for el in susjedi:
        patterns_i.add(el)
    for r in patterns_i:
      patterns.append(r)
  
  rezultat=[]
  for el in patterns:
    if  patterns.count(el)==len(dna): 
      rezultat.append(el)
  rezultat=list(set(rezultat)) #izbacimo duplikate
  for i in range(len(rezultat)):
    print(rezultat[i], end=" ")
