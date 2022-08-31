def ChromosomeToCycle(chromosome):
  ciklus=[]
  for el in chromosome:
    if el>0:
      ciklus.append(2*el-1)
      ciklus.append(2*el)
    else:
      ciklus.append(-2*el)
      ciklus.append(-2*el-1)
  return ciklus
