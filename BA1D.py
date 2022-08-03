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
  revcomplement=complement[::-1]
  return revcomplement

# trazimo dio koda ili njegovog komplementa u genomu
# tj trazimo indekse u genomu gdje se kao podstring pojavljuje pattern ili njegov reverzni komplement
def PatternMatching(pattern,genome):
  p = "" # prazni string na koji cemo dodavat pocetne pozicije koje pronademo
  for i in range(len(genome) - len(pattern)+1):
	  if (genome[i:i+len(pattern)] == pattern) or (genome[i:i+len(pattern)] == ReverseComplement(pattern)):
		  p += str(i) + " " #dodajemo indeks i razmak jer nam rjesenje mora bit u tom obliku

  print(p)
  return p

