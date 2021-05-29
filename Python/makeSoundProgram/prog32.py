import time
def koan(sentence):
  parts = sentence.lower().split() #splits the sentence into separate strings for array
  subject = parts[0]
  verb = parts[1]
  object = parts[2]
  print "Sometimes "+sentence+"."
  print "But sometimes, " +object+" "+verb+" "+subject
  print "Sometimes, there is no "+subject
  print "Other times, there is no "+object
  print "Very rarely, there is no " +verb
  time.sleep(3)
  print "WATCH OUT!!!!"
  
  