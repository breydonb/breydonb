def mainFn():
  img = makePicture(r"C:\Users\B226-05\Desktop\buffalos.jpg")
  distanceFn(img,.5,.5,2,75) #change values for multipliers
  explore(img)
  #writePictureTo(img, r"C:\Users\B226-05\Desktop\coolBuffalos.jpg")

def distanceFn(img,rMulti,gMulti,bMulti,distanceInt):
  #buffColor = makeColor(125,80,50)
  buffLeg = makeColor(24,22,23)
  for i in getPixels(img):
    theColor = getColor(i)
    if distance(theColor,buffLeg) <= distanceInt:
      iRed = getRed(i)*rMulti
      iGreen = getGreen(i) *gMulti
      iBlue = getGreen(i)*bMulti
      setColor(i, makeColor(iRed,iGreen,iBlue))
    