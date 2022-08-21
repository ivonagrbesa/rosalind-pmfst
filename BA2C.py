def NapraviMatricu(profile):
  profile=profile.split("\n") #razdvoji na retke
  for i in range(0, len(profile)): #svaki redak
    profile[i]=[float(n) for n in profile[i].split()] #splitaj po razmaku i sve iz tog niza pretvori u float

  return profile

def KmerProbability(kmer, profile):
  probs=[] #niz vjerojatnosti za svako slovo
  rj=1
  for i in range(0, len(kmer)):
    if kmer[i]=="A":
      probs.append(profile[0][i])
    elif kmer[i]=="C":
      probs.append(profile[1][i])
    elif kmer[i]=="G":
      probs.append(profile[2][i])
    elif kmer[i]=="T":
      probs.append(profile[3][i])
  for p in probs:
    rj=rj*p
  return rj    

def MostProbableKmer(text, k, profile):
  D=dict() #u dict spremamo sve kmere i njihove vjr
  for i in range(0, len(text)-k+1):
    rijec=text[i:i+k]
    p=KmerProbability(rijec, profile)
    D[rijec]=p
  
  m=max(D.values()) #nademo najvecu vjr
  for i in D.items():
    if i[1]==m: #onaj item koji ima najvecu vjr
      print(i[0]) #isprintaj taj string s najvecom vjr
      break
