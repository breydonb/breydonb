#Breydon Brennan 9/6/19
#Compound Interest Fn

def mainFn(pctVar,nVar,principalVar):

  calcFn(pctVar,nVar,principalVar)  #in order to put the args into another function, you must redefine the variables in the second function and include them when you call it
  
  # Ex: If you have 3 arguments, you must define them in both functions. Then, when you call the second function, you must have 3 arguments.
  # If you do not, you will get this error: The error was: calcFn() takes at least 3 arguments (0 given)
  # args must always be equal!!! 
  
def calcFn(pctVar,nVar,principalVar):
  newPercent= float(pctVar)/100
  compoundInterest= principalVar*(1+newPercent)**nVar
  
  compoundInterest= int(compoundInterest)
  
  print "In "+str(nVar)+" years at "+str(pctVar)+"%, you would have a $"+str(compoundInterest)+".00 with $"+str(principalVar)+ " as your initial investment."