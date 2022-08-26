def OverlapGraph2(patterns):
  D=dict()
  for i in range(len(patterns)):
    for j in range(len(patterns)):
      if i!=j and patterns[i][1:]==patterns[j][:-1]:
        D[patterns[i]]=patterns[j]
  for i in D.items():
    print(i[0] + " -> " + i[1])
