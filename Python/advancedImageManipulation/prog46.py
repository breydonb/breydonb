def mainFn():
  img = makePicture(r"C:\Users\B226-05\Desktop\buffalos.jpg")
  #copyHalf(img)
  mirrorHalf(img)
  print "The width of image is " + str(getWidth(img))
  print "The height of image is " + str(getHeight(img))
  explore(img)
  
def copyHalf(img):
  pxlArray = getPixels(img)
  for i in range(0,(len(pxlArray)/2)):
    currentPxl = pxlArray[i]
    pxlColor = getColor(currentPxl)
    two_pixel = pxlArray[i + (len(pxlArray)/2)]
    setColor(two_pixel, pxlColor)
    
def mirrorHalf(img):
  pxl = getPixels(img)
  target = len(pxl)-1
  for i in range(0, (len(pxl)/2)):
    pxl1 = pxl[i]
    color1= getColor(pxl1)
    pxl2 = pxl[target]
    setColor(pxl2, color1)
    target = target - 1