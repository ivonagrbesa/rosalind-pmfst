def ChromosomeToCycle(chromosome):
  cycle=[]
  for el in chromosome:
    if el>0:
      cycle.append(2*el-1) #tail
      cycle.append(2*el) #head
    else:
      cycle.append(-2*el) #head
      cycle.append(-2*el-1) #tail
  return cycle


def ColoredEdges(P):
  edges=[]
  for kromosom in P:
    ciklus=ChromosomeToCycle(kromosom) #svaku perm pretvorimo u ciklus
    for i in range(1, len(ciklus),2):
      if i!=len(ciklus)-1:
        edges.append((ciklus[i], ciklus[i+1]))
      else:
        edges.append((ciklus[i], ciklus[0]))
  
  return edges
