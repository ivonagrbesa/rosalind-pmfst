def PatternCount(Text, Pattern):
  count=0
  for i in range (0, (len(Text)-len(Pattern)+1)):
    if (Text[i: i+len(Pattern)]==Pattern):
      count=count+1
  return count

# fja za trazenje maksimuma niza
def Maks(niz):
  maks=niz[0]
  for i in range(0,len(niz)):
    if (niz[i]>maks):
      maks=niz[i]
  return maks

def FrequentWords(Text, k):
  Count=[0]*(len(Text)-k+1)
  FrequentPatterns=[]
  for i in range(0, len(Text)-k+1):
    Pattern=Text[i:i+k]
    Count[i]=PatternCount(Text, Pattern)
  maxCount=Maks(Count)
  for i in range(0, len(Text)-k+1):
    if Count[i]==maxCount:
      FrequentPatterns.append(Text[i:i+k])
  FrequentPatterns=list(dict.fromkeys(FrequentPatterns))
  return FrequentPatterns
