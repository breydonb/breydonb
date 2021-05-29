#Breydon Brennan 9/9/19
#Page 50 prog14


def parts(string):
  for letter in string:
    print letter
    
def count(string):
  counterVar=0
  for i in string:
    counterVar = counterVar + 1
   
  print str(counterVar)

#See prog15 p. 51 using  
def sortLoop(string):
  pileLowers=""
  pileUppers=""
  pileDigits=""
  pileSpecial=""
  
  for i in string:
    if i in "0123456789":
      pileDigits=i+pileDigits
    elif i in 'abcdefghijkmnopqrstuvwxyz':
      pileLowers=i+pileLowers
    elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      pileUppers= i+pileUppers
    else:
      pileSpecial= i+pileSpecial
  
  print "Digits: " +pileDigits
  print "Lowers: " +pileLowers
  print "Uppers: " +pileUppers
  print "Special: " +pileSpecial
  
def sortLoop2(string):
  pileLowers=""
  pileUppers=""
  pileDigits=""
    
  for i in string:
    if i in "0123456789":
      pileDigits=i+pileDigits
    elif i in 'abcdefghijkmnopqrstuvwxyz':
      pileLowers=i+pileLowers
    elif i.lower() in 'abcdefghijkmnopqrstuvwxyz':
      pileUppers= i+pileUppers
    
  
  print "Digits: " +pileDigits
  print "Lowers: " +pileLowers
  print "Uppers:" +pileUppers
  