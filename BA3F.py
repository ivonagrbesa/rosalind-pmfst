def NapraviDict(graf):
  D=dict()
  graf=graf.split("\n")
  for brid in graf:
    kljuc, vrij=brid.split(" -> ")
    vrij=vrij.split(",")
    D[kljuc]=vrij
  return D

def EulerianCycle(D):
  pocetni=list(D.keys())[0] #prvi vrh koji imamo
  trenutni=pocetni
  ciklus=[pocetni]

  while D: #dok imamo vrhova
    if trenutni in D: #ako mozemo nastavit iz zadnjeg vrha
      ciklus.append(D[trenutni][0])
      if len(D[trenutni])==1:
        del D[trenutni]
      else:
        del D[trenutni][0]
      trenutni=ciklus[-1] 
    
    else: #ako ne mos vise nastavit ciklus iz zadnjeg vrha
      for (i, el) in enumerate(ciklus):
        if el in D: #ako nademo u ciklusu neiskoristeni vrh (tj da je jos u D)
          noviciklus=ciklus[i:-1] + ciklus[:i+1] #onda pocnimo novi ciklus od njega
          ciklus=noviciklus
          trenutni=el #i iz njega trazimo neki dodatni ciklus
          break
  
  return ciklus
