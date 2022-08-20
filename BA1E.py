def FindClumps(genome, k, L, t):
  clumps=dict()
  for i in range(0, len(genome)-L+1):
    prozor=genome[i:i+L]
    kmeri_prozor=dict()
    for j in range(i, i+L-k+1):
      kmer=genome[j:j+k] #kmer iz prozora
      if kmer in kmeri_prozor:
        kmeri_prozor[kmer]+=1
      else:
        kmeri_prozor[kmer]=1
    
    for x in kmeri_prozor.items():
      if x[1]>=t: #ako se pojavio u prozoru bar t puta => to je clump
        if x[0] in clumps: #ako je taj kmer vec bio clump u nekom drugom prozoru
          clumps[x[0]]+=1
        else:
          clumps[x[0]]=1
  return clumps
