def ChromosomeToCycle(chromosome):
  cycle=[]
  for el in chromosome:
    if el>0: #tail,head
      cycle.append(2*el-1)
      cycle.append(2*el)
    else: #(head,tail)
      cycle.append(-2*el)
      cycle.append(-2*el-1)
  return cycle

def ColoredEdges(P):
  edges=[]
  for kromosom in P: #svaki kromosom pretvorimo u ciklus
    ciklus=ChromosomeToCycle(kromosom)
    for i in  range(1, len(ciklus),2):
      if i!=len(ciklus)-1:
        edges.append([ciklus[i], ciklus[i+1]])
      else:
        edges.append([ciklus[i], ciklus[0]])
  return edges

def NadiSljedeci(trenutni, edges): #trazi slj brid medu obojanim bridovima s obz na trenutni
  if len(edges)==0:
    return -1
  idx=0
  while not (trenutni[0] in edges[idx] or trenutni[1] in edges[idx]):
    idx+=1
    if idx==len(edges):
      return -1
  return edges[idx] #vrati onaj obojani brid di smo se zaustavili

def CycleToChromosome(ciklus):
  kromosom=[] #ovo ce bit niz synteny blokova
  for i in range(0, len(ciklus), 2):
    if ciklus[i]<ciklus[i+1]: #ako tail,head
      kromosom.append(ciklus[i+1]//2)
    else: #ako head,tail
      kromosom.append(-ciklus[i]//2)
  return kromosom

# za trazenje ciklusa u grafu
def NadiSljedeci2(trenutni, edges):
  if len(edges)==0:
    return -1
  idx=0
  val=trenutni[1] #kraj  trenutnog brida
  if val%2==0: #ako je taj kraj paran br
    val-=1 #smanji ga za 1 da postane neparan
  else:
    val+=1 #ako je neparan, povecaj ga za 1 da postane paran

  while not val in edges[idx]: #dok god se taj kraj ne nalazi u edges[idx] odn sljedecem bridu
    idx+=1 #pomici se po tim slj bridovima
    if idx==len(edges): #sve dok ne dodes do kraja
      return -1
  if val == edges[idx][1]: #kad pronademo taj kraj u nekom bridu i to kao kraj nekog brida
      edges[idx].reverse() #okreni taj  brid
  return edges[idx]


def GraphToGenome(graph):
  kromosomi=[] #tj genom
  ciklusi=[]
  idx=0

  while len(graph)>0:
    ciklus=[] #
    trenutni=graph[0] #ovo je niz od 2el
    while trenutni!=-1: #dok ne potrosimo sve cvorove
      ciklus+=trenutni #uniramo prazni ciklus sa trenutnim
      graph.remove(trenutni)
      sljedeci=NadiSljedeci2(trenutni, graph)
      trenutni=sljedeci
    #ako smo  potrosili sve cvorove,zavrsili smo ciklus
    ciklusi.append(ciklus)
  
  for c in ciklusi:
    c=[c[-1]]+c[:-1] #zapisi svaki ciklus td pocinje zadnjim elementom
    kromosom=CycleToChromosome(c)
    kromosomi.append(kromosom)
  
  return kromosomi



# trazimo netriv cikluse  u breakpoint grafu
def NadiCikluse(edges):
  ciklusi=[] #ovdi dodajemo netriv.cikluse (duljine >2)

  while len(edges)>0:
    start=edges[0]
    edges.remove(edges[0])
    trenutni=NadiSljedeci(start, edges)
    ciklus=[start]
    while trenutni!=-1: #dok ne dodemo do kraja ciklusa
      ciklus.append(trenutni)
      edges.remove(trenutni)
      trenutni=NadiSljedeci(trenutni, edges)
    if len(ciklus)>2:
      ciklusi.append(ciklus) #dodamo ga ako je netrivijalan

  return ciklusi


# ako napravimo 2 break na obojanom grafu
def TwoBreakOnGenomeGraph(genomeGraph, i1, i2, i3, i4):
  if [i1, i2] in genomeGraph: #ako imamo brid [i,i']
    for i in range(len(genomeGraph)):
      if genomeGraph[i]==[i1, i2]:
        genomeGraph[i]=[i1,i3] # [i,i']=> [i,j]
  else:
    for i in range(len(genomeGraph)):
      if genomeGraph[i]==[i2,i1]: #ako nemamo [i,i'] trazimo ima li [i',i]
        genomeGraph[i]=[i3, i1] #[i',i]=>[j,i]
  
  if [i3,i4] in genomeGraph: #ako imamo [j,j'] negdi u grafu
    for i in range(len(genomeGraph)):
      if genomeGraph[i]==[i3,i4]:
        genomeGraph[i]=[i2, i4] # [j,j']=>[i',j']
  else: 
    for i in range(len(genomeGraph)):
      if genomeGraph[i]==[i4,i3]: #ako nema [j,j'], gledamo ima li [j',j]
        genomeGraph[i]=[i4, i2] # [j',j]=>[j', i']

  return genomeGraph  


# ako napravimo 2 break na kromosomu/genomu
# izvodimo 2 break na obojanim bridovima pa prvo moramo pronac  njih
def TwoBreakOnGenome(genom, i1, i2, i3, i4):
  genomeGraph=ColoredEdges(genom)
  genomeGraph=TwoBreakOnGenomeGraph(genomeGraph, i1, i2, i3, i4)
  rj=GraphToGenome(genomeGraph) #graf vratimo nazad u genom
  return rj


def ShortestTransformation(P,Q):
  rj=[P] 
  redEdges=ColoredEdges(P)
  blueEdges=ColoredEdges(Q)
  breakpointGraph=redEdges+blueEdges #uniramo crvene i plave bridove

  ciklusi=NadiCikluse(breakpointGraph)
  while len(ciklusi)>0:

    netrivCiklus=ciklusi[0]
    for i in range(0, len(netrivCiklus)-1):
      if netrivCiklus[i][0] in netrivCiklus[i+1]:
        netrivCiklus[i].reverse()
      if netrivCiklus[i+1][1] in netrivCiklus[i]:
        netrivCiklus[i+1].reverse()
    
    idx=0

    while not netrivCiklus[idx] in redEdges:
      idx+=1
    i1,i2=netrivCiklus[idx]

    if idx+2!=len(netrivCiklus):
      i3, i4=netrivCiklus[idx+2]
    else:
      i3, i4=netrivCiklus[0]
    
    redEdges.remove([i1,i2])
    redEdges.remove([i3,i4])
    redEdges.append([i1, i4])
    redEdges.append([i2,i3])

    breakpointGraph=redEdges+blueEdges #ponovo uniramo ali sad su to novi bridovi
    ciklusi=NadiCikluse(breakpointGraph) 
    P=TwoBreakOnGenome(P, i1, i2, i3, i4)
    rj.append(P)

  return P



  
  
  
