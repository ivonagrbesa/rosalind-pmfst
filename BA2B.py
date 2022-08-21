import itertools

def HammingDistance(s1, s2):
  d=0
  for i in range(len(s1)):
    if s1[i]!=s2[i]:
      d+=1
  return d

def PatternDnaiDistance(pattern, dnai):
  k=len(pattern)
  d=[]
  for i in range(len(dnai)-k+1):
    pattern2=dnai[i:i+k]
    d.append(HammingDistance(pattern, pattern2))
  m=min(d)
  return m

def PatternDnaDistance(pattern, dna):
  d=0
  for linija in dna:
    d+=PatternDnaiDistance(pattern, linija)
  return d

def MedianString(dna, k):
  sviKmeri=map(''.join, itertools.product('ACGT', repeat=k))
  udaljenosti=dict()
  for kmer in sviKmeri:
    udaljenosti[kmer]=PatternDnaDistance(kmer, dna)

  m=min(udaljenosti.values())
  for i in udaljenosti.keys():
    if udaljenosti[i]==m:
      print(i)
      break
