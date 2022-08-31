def TwoBreakOnGenomeGraph (graph, i1, i2, i3, i4):
  if [i1, i2] in graph:
    for i in range(len(graph)):
      if graph[i]==[i1, i2]:
        graph[i]=[i1, i3]
  else:
    for i in range(len(graph)):
      if graph[i]==[i2, i1]:
        graph[i]=[i3, i1]
  
  if [i3, i4] in graph:
    for i in range(len(graph)):
      if graph[i]==[i3, i4]:
        graph[i]=[i2, i4]
  else:
    for i in range(len(graph)):
      if graph[i]==[i4, i3]:
        graph[i]=[i4, i2]
  return graph
