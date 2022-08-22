def HD(string1, string2):
  d=0
  for i in range(len(string1)):
    if string1[i]!=string2[i]:
      d+=1
  return d

def DistancePatternStrings(pattern, dna):
  k=len(pattern)
  d=0
  for linija in dna:
    hd=5000
    for i in range(0, len(linija)-k+1):
      pattern2=linija[i:i+k]
      if HD(pattern, pattern2)<hd:
        hd=HD(pattern, pattern2)
    d=d+hd
  return d
