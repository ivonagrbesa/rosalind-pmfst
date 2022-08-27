graf=''''''

def NapraviDict(graf):
  D=dict()
  graf=graf.split("\n")
  for el in graf:
    kljuc, vrij=el.split(" -> ")
    vrij=vrij.split(",")
    D[kljuc]=vrij
  return D

G=NapraviDict(graf)

def EulerianCycle(D):
  pocetni=list(D.keys())[0]
  trenutni=pocetni
  ciklus=[pocetni]

  while D:
    if trenutni in D:
      ciklus.append(D[trenutni][0])
      if len(D[trenutni])==1:
        del D[trenutni]
      else:
        del D[trenutni][0]
      trenutni=ciklus[-1]
    else:
      for i,el in enumerate(ciklus):
        if el in D:
          noviciklus=ciklus[i:-1]+ciklus[:i+1]
          ciklus=noviciklus
          trenutni=el #taj el koji ima neiskoristenih bridova => iz njega nastavi trazit
          break
  return ciklus



from collections import Counter

def Izbalansiraj(graph): 
  graph=graph.copy() #kopiramo graf jer cemo morat usporedit s onim sta je bilo na pocetku
  izlazni={k: len(graph[k]) for k in graph.keys()}
  ulazni_list=[]
  for v in graph.values():
    ulazni_list.extend(v)
  ulazni=Counter(ulazni_list)

  svicvorovi=set(list(izlazni.keys())+list(ulazni.keys()))

  for cvor in svicvorovi:
    balance=izlazni.get(cvor, 0)-ulazni.get(cvor, 0)
    if balance==1: #to je pocetak puta, odn kraj novog brida
      second=cvor
    if balance==-1: #to je kraj puta, odn pocetak novog dodanog brida
      first=cvor
    
  if first not in graph:
    graph[first]=[second]
  else:
    graph[first].append(second)
  
  return graph, first, second #vraca balansirani graf i nebalansirane cvorove koje smo sad spojili



g, first, second=Izbalansiraj(G) # u izbalansiranom grafu moze se pronaci E.ciklus
ciklus=EulerianCycle(g)[:-1]

for i in range(len(ciklus)):
  if ciklus[i]==first and ciklus[(i+1)%len(ciklus)]==second: # vrhovi izmedu kojih je povucen novi brid
    rj=ciklus[i+1:] + ciklus[:i+1] #poceli bi vrhom second(pocetak puta) i zavrsili sa first(kraj puta)

# rj je E.put
print("->".join(rj))
