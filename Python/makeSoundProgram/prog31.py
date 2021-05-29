#Breydn Brennan
#Program 31 on page 63
#9/4/19

def decodeFn(secret,keyletters):
  alpha="abcdefghijklmnopqrstvwxyz" #you must specify the alphabet to the computer
  clear=""
  for letter in secret:
    index = keyletters.find(letter)
    clear = clear+alpha[index]
  print clear
  
def encodeFn(string, keyletters): #For every decoding function, you need to include the encoder
  alpha="abcdefghijklmnopqrstvwxyz"
  secret = ""
  for letter in string:
    index = alpha.find(letter)
    secret = secret+keyletters[index]
  print secret
  
def buildCipher(key):
  alpha="abcdefghijklmnopqrstvwxyz"
  rest=""
  for letter in alpha:
    if not(letter in key):
      rest = rest + letter
  print key+rest