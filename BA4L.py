integerMassTable={'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
              'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}

def IzracunajMasu(peptide):
  masa=0
  slova=list(peptide) #od stringa napravimo listu
  for s in slova:
    masa+=integerMassTable[s]
  return masa

def LinearSpectrum(peptide):
  spektar=[0] #prazni peptid (triv.)

  for i in range(1, len(peptide)): #netrivijalni podstringovi
    for j in range(0, len(peptide)):
      if j+i<=len(peptide):
        m=IzracunajMasu(peptide[j:j+i])
        spektar.append(m)
  
  spektar.append(IzracunajMasu(peptide)) #cijeli string  (triv.)
  spektar.sort() #uzlazno
  return spektar


def LinearScore(peptide, Spectrum):
  linearnispektar=LinearSpectrum(peptide)
  score=0

  sve=set(linearnispektar+Spectrum)
  for el in sve:
    score+=min(linearnispektar.count(el), Spectrum.count(el))
  return score



def Trim(leaderboard, spectrum, N):
  if len(leaderboard)<N:
    return leaderboard
  
  linearscores=[0]*(len(leaderboard)) 
  for j in range(len(leaderboard)):
    peptide=leaderboard[j]
    linearscores[j]=LinearScore(peptide, spectrum)
  
  linearscores.sort() #sortirali linearne scoreove uzlazno
  linearscores.reverse() #i obrnili to => sad je silazno

  granica=linearscores[N-1] 
  
  rj=[]

  for el in leaderboard:
    if LinearScore(el, spectrum)>=granica:
      rj.append(el)
  print(*rj)
