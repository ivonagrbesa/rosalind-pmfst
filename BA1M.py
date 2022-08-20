def NumberToSymbol(broj):
  if broj==0:
    return "A"
  elif broj==1:
    return "C"
  elif broj==2:
    return "G"
  elif broj==3:
    return "T"
  
def NumberToPattern(index, k):
  if k==1:
    return NumberToSymbol(index)
  prefixIndex=index//4 #brojcana vrijednost prefiksa => pretvorimo to u (k-1)-mer tj prefiks
  r=index%4 #brojcana vrijednost ostatka (0,1,2 ili 3)
  symbol=NumberToSymbol(r) #zadnje slovo
  prefixPattern=NumberToPattern(prefixIndex, k-1)
  return prefixPattern+symbol
