def BreakpointsNumber(P):
  rj=0
  P=[0]+P+[len(P)+1] #dodamo 0 i n+1
  for i in range(0, len(P)-1):
    if P[i+1]-P[i]!=1:
      rj+=1
  return rj
