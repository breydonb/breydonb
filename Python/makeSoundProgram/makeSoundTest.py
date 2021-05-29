def mainFn(driveLetter, whichSound):
  if whichSound == "no deal":
    sndFilePath=driveLetter+':\\Users\\B226-05\\Desktop\\no_deal.wav'
    playSound(sndFilePath)
  elif whichSound == "you die":
    sndFilePath=driveLetter+':\\Users\\B226-05\\Desktop\\carlitos_way_you_die.wav'
    playSound(sndFilePath)
  else:
    print "You must choose a valid sound: 'you die' or 'no deal'"
#################################################
def playSound(sndFilePath):
  play(makeSound(sndFilePath))
#################################################