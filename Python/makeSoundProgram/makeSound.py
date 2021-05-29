from time import sleep
#Breydon Brennan
#8-23-19
#How pickAFile()works with audio files
##################################

def mainFn():
  #sndPath=pickAFile()
  #print sndPath
  sndPath= 'C:\\Users\\B226-05\\Desktop\\no_deal.wav'
  autoSong(sndPath)
  sleep(2)
  autoSong('C:\\Users\\B226-05\\Desktop\\carlitos_way_you_die.wav')
  
##################################
#Another way to handle file references...

def fullAutoSong(): #no arg. sndPath is hard coded
  sndPath= 'C:\\Users\\B226-05\\Desktop\\no_deal.wav'
  play(makeSound(sndPath))
  

##################################
#First pickAFile() and then use as arg

def autoSong(sndPath): #sndPath is a arg
  play(makeSound(sndPath))
  
##################################

def playSong():
  play(makeSound(pickAFile()))