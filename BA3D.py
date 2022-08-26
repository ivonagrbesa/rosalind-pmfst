def DeBruijn(k, text):
  D=dict()
  for i in range(0, len(text)-k+1):
    kmer=text[i:i+k]
    prefiks=kmer[:-1]
    sufiks=kmer[1:]
    if prefiks not in D:
      D[prefiks]=[sufiks]
    else: #ako otprije imamo taj kljuc
      D[prefiks].append(sufiks) #ne dodajemo ga opet, nego mu u value samo dodamo novi sufiks => to je ka da zalipimo iste vrhove zajedno
  
  kljucevi=sorted(D.keys())
  for k in kljucevi:
    print(k + " -> " + ",".join(sorted(D[k])))

# i kljucevi i njihove vrijednosti moraju bit sortirane leksikografski
