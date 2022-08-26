def DeBruijn(patterns):
  D=dict()
  for p in patterns:
    prefiks=p[:-1]
    sufiks=p[1:]
    if prefiks not in D:
      D[prefiks]=[sufiks]
    else: #ako je taj prefiks vec u kljucevima, onda on vec ima nesto u svom  nizu pa samo appendamo novi sufiks
      D[prefiks].append(sufiks)
  
  kljucevi=sorted(D.keys())
  for k in kljucevi:
    print(k + " -> " + ",".join(sorted(D[k])))
