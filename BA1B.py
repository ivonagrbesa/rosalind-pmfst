def PatternCount(Text, Pattern):
  count=0
  for i in range (0, (len(Text)-len(Pattern)+1)):
    if (Text[i: i+len(Pattern)]==Pattern):
      count=count+1
  return count

def MostFreqWords(text, k):
  rj=set()
  frekvencije=[0]*(len(text)-k+1)
  for i in range(len(text)-k+1):
    kmer=text[i:i+k]
    frekvencije[i]=PatternCount(text, kmer)
  m=max(frekvencije)
  for i in range(len(text)-k+1):
    if frekvencije[i]==m:
      rj.add(text[i:i+k])
  return rj
