import itertools

def dNeighborhood(pattern, d):
  k=len(pattern)
  sviKmeri=map(''.join, itertools.product('ACGT', repeat=k))
  rj=[]
  for el in sviKmeri:
    if HammingDistance(pattern, el)<d:
      rj.append(el)
  return rj
 
rj=dNeighborhood("GTACGAGTATC",3)
for el in rj:
  print(el)
  
  
# ili drugi nacin
#BA1N rj iz skripte
def Neighbors(pattern, d):
  nukleotidi=["A", "C", "G", "T"]
  if d==0:
    return pattern
  if len(pattern)==1:
    return {"A", "C", "G", "T"}
  n=set()
  suffixn=Neighbors(pattern[1:], d)
  for el in suffixn:
    if HammingDistance(pattern[1:], el)<d:
      for slovo in nukleotidi:
        n.add(slovo+el)
    else:
      n.add(pattern[0]+el)
  return n
