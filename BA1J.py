#pomocno
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

def ReverseComplement(pattern):
  rc=""
  for slovo in pattern:
    if slovo=="A":
      rc+="T"
    elif slovo=="C":
      rc+="G"
    elif slovo=="G":
      rc+="C"
    elif slovo=="T":
      rc+="A"
  return rc[::-1]

#BA1J
def FreqWMismatchesRC(text, k, d):
  rj=""
  D=SviKmeri(k)
  for i in range(len(text)-k+1):
    rijec=text[i:i+k]
    for el in D.items():
      rc=ReverseComplement(el[0])
      if HammingDistance(el[0], rijec)<=d:
        D[el[0]]+=1
      if HammingDistance(rc, rijec)<=d:
        D[el[0]]+=1
  
  m=max(D.values())
  for el in D.keys():
    if D[el]==m:
      rj=rj+el+" "
  return rj
