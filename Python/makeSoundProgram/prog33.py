import time
def koan2(sentence):
  parts = sentence.lower().split()
  verbindex = 1
  objindex = 2
  subject = parts[0]
  if subject in ["the","a","an"]:
    subject =parts[1]
    verbindex = 2
    objindex = 3
  verb = parts[verbindex]
  object = parts[objindex]
  
  if object in ["the","a","an"]:
    object = parts[4]
    
  print "Sometimes "+sentence
  print "But sometimes, " +object+ " "+verb+" "+subject
  print "Sometimes there is no "+subject
  print "Sometimes there is no "+verb
  time.sleep(3)
  print "Watch out"
   
  