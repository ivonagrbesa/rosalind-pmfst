def DPChange(money, Coins):
  MinNumCoins=[0]*(money+1) 
  for m in range (1, money+1): #po mogucem iznosu novca za vratiti, ne diramo 0.indeks jer 0 svakako vracamo s 0 novcica
    MinNumCoins[m]=m+1 #umjesto besk.
    for i in Coins: #po denominacijama
      if i<=m: #ako je i-ta denominacija manja od iznosa koji vracamo
        if MinNumCoins[m-i]+1<MinNumCoins[m]:
          MinNumCoins[m]=MinNumCoins[m-i]+1
  return MinNumCoins[money]
