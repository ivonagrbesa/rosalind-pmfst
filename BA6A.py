def kSortReversal(P, k): # sredujemo k-tu poziciju
  j=k
  while P[j]!=k+1 and P[j]!=-(k+1):
    j+=1
  P[k:(j+1)]=[-1*x for x in P[k:(j+1)]][::-1]
  return P


def GreedySort(P):
  d=0 #kad god napravimo ksort, povecamo d
  for k in range(0, len(P)):
    if P[k]!=k+1:
      P=kSortReversal(P, k)
      d+=1
      print("(" + " ".join(["+"+str(el) if el>0 else str(el) for el in P]) + ")")
      if P[k]==-(k+1):
        P=kSortReversal(P, k)
        d+=1
        print("(" + " ".join(["+"+str(el) if el>0 else str(el) for el in P]) + ")")
  return d

