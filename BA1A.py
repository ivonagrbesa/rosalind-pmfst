def PatternCount(Text, Pattern):
  count=0
  for i in range (0, (len(Text)-len(Pattern)+1)):
    if (Text[i: i+len(Pattern)]==Pattern):
      count=count+1
  return count
