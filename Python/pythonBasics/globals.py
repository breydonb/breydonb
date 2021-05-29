#Breydonb
#demo of global variables

def mainFn():
  global coffee #prototype a global variable. DANGER!!!!
  coffee= "goodstuff"
  
  print coffee
  bigFn()
  print coffee
  
def bigFn():
  global coffee
  print coffee
  coffee="battery acid"