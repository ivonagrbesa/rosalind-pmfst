def HammingDistance(string1, string2):
  d=0
  for i in range(0, len(string1)):
    if string1[i]!=string2[i]:
      d=d+1
  return d

def ApproximatePattern(pattern, text, d):
    positions = []
    for i in range(len(text)-len(pattern)+1):
        if HammingDistance(pattern, text[i:i+len(pattern)]) <= d:
            print(i, end=" ")
            positions.append(i)
    return positions
