def MinSkew2(genome):
  skews=[0]
  for i in range(0, len(genome)):
    if genome[i]=="G":
      skews.append(skews[-1]+1) #zadnjeg iz niza povecaj za 1 i dodaj
    elif genome[i]=="C":
      skews.append(skews[-1]-1) #zadnjeg iz niza smanji za 1 i dodaj
    else:
      skews.append(skews[-1]) #ako nije G ni C onda skew ostaje isti pa samo ponovi zadnji el
  
  m=min(skews) #minimalni skew
  for i in range(len(skews)):
    if skews[i]==m:
      print(i, end=" ")
