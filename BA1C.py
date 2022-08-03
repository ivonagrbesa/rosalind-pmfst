def ReverseComplement(Pattern):
  complement=""
  for i in range(0, len(Pattern)):
    if Pattern[i]=="A":
      complement+="T"
    if Pattern[i]=="T":
      complement+="A"
    if Pattern[i]=="C":
      complement+="G"
    if Pattern[i]=="G":
      complement+="C"
  revcomplement=complement[::-1] #pocni od kraja stringa, zavrsi na indeksu 0, s korakom -1 (unatrag)
  return revcomplement
