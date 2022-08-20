pattern="GCAAATCCTCGCTGTAGTGTCTGG";

def SymbolToNumber(simbol):
  if simbol=="A":
    simbol=0
  if simbol=="C":
    simbol=1
  if simbol=="G":
    simbol=2
  if simbol=="T":
    simbol=3
  return simbol


def Rekurzija(pattern):
  if len(pattern)==0:
    return 0
  while len(pattern)>0:
    symbol=pattern[-1]
    prefix=pattern[-len(pattern):-1]
    return 4*Rekurzija(prefix)+SymbolToNumber(symbol)

print (Rekurzija(pattern))
