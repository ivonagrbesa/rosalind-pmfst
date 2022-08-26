def KmerComposition(text, k):
  rj=[]
  for i in range(0, len(text)-k+1):
    kmer=text[i:i+k]
    rj.append(kmer)
    #rj=sorted(rj) moze i sortirano a i ne mora
  for el in rj:
    print(el)
