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

def ComputingFrequencies(text,k):
  FreqArray=[0]*(4**k) #frekvencije svih k-mera
  for i in range(len(text)-k+1):
    pattern=text[i:i+k]
    j=PatternToNumber(pattern) #pattern pretvorili u njegov redni br tj njegov indeks u FreqArray
    FreqArray[j]+=1
  return FreqArray
