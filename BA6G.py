def CycleToChromosome(ciklus):
  kromosom=[]
  for i in range(0, len(ciklus),2):
    if ciklus[i]<ciklus[i+1]:
      kromosom.append(ciklus[i+1]//2)
    else:
      kromosom.append(-ciklus[i]//2)
  return kromosom


# pozitivnim elementima niza dodaje + isprid
def DodajPlus(ciklus):
  noviciklus=[]
  for el in ciklus:
    if el>0:
      noviel="+"+str(el)
    else:
      noviel=str(el)
    noviciklus.append(noviel)
  return noviciklus
