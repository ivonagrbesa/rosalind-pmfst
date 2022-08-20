def HammingDistance(s1,s2):
  d=0
  for i in range(len(s1)):
    if s1[i]!=s2[i]:
      d+=1
  return d

import itertools

def SviKmeri(k):
  kmeri=map(''.join, itertools.product('ACGT', repeat=k)) #ovo je map object (izgleda slicno ka dict)
  rj=dict()
  for kmer in kmeri:
    rj[kmer]=0
  return rj
# dictionary svih k-mera sa slovima ACGT, svi imaju value 0

def FreqWMismatches(text, k, d):
  rj=""
  D=SviKmeri(k) #ovo je dict
  for i in range(0, len(text)-k+1):
    rijec=text[i:i+k]
    for i in D.items():
      if HammingDistance(i[0], rijec)<=d:
        D[i[0]]+=1
  
  vrijednosti=D.values() 
  m=max(vrijednosti) #maks broj d-susjeda
  for kljuc in D.keys():
    if D[kljuc]==m: #ako neki string ima maks broj d-susjeda
      rj+=kljuc+" "
  return rj
