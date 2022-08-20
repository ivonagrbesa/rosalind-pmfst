def SymbolToNumber(slovo):
  if slovo=="A":
    return 0
  elif slovo=="C":
    return 1
  elif slovo=="G":
    return 2
  else: #T
    return 3

def PatternToNumber(pattern):
  if len(pattern)==0:
    return 0
  simbol=pattern[-1] #zadnje slovo
  prefix=pattern[:-1] #sve do zadnjeg slova
  return 4*PatternToNumber(prefix)+SymbolToNumber(simbol)
