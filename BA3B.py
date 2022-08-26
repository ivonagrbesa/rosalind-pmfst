def ReconstructString(patterns):
  text=""
  text+=patterns[0] #prvi kmer cili
  for i in range(1, len(patterns)): #a od svih ostalih
    text+=patterns[i][-1] #samo zadnje slovo
  return text
