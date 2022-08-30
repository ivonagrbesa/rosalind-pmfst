def NapraviDown(down):
  rez=[]
  down=down.split("\n")
  for i in range (n): #jer ima n redaka
    sniz=down[i].split() #splitani niz
    rj=[int(x) for x in sniz]
    rez.append(rj)
  return rez

def NapraviRight(right):
  rez=[]
  right=right.split("\n")
  for i in range(1, n+2): #jer ima n+1 redaka (preskocimo prvi niz jer je tu samo \n tj prazni navodnici)
    sniz=right[i].split()
    rj=[int(x) for x in sniz]
    rez.append(rj)
  return rez


def ManhattanTourist(n, m, Down, Right):
  s=[] #matrica putova(udaljenosti)
  for i in range(n+1): #za svaki redak na karti
    s.append([0]*(m+1)) #dodaj niz od m+1 nula

  for i in range(1, n+1):
    s[i][0]=s[i-1][0]+Down[i-1][0]

  for j in range(1, m+1):
    s[0][j]=s[0][j-1]+Right[0][j-1]
    
  for i in range(1, n+1):
    for j in range(1, m+1):
      s[i][j]=max(s[i-1][j]+Down[i-1][j], s[i][j-1]+Right[i][j-1])
  return s[n][m] #vracamo zadnji el matrice
