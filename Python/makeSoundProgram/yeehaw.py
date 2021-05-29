def mainFn(string):
  pileFront=""
  pileBack=""
  pileRev=""
  
  for i in range(0,len(string)/2):
    pileFront= pileFront+string[i]
  
  for i in range(len(string)/2,len(string)):
    pileBack= pileBack+string[i]
    
  print pileFront
  print pileBack