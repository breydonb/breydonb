def mainFn(cmdArg,sPath):
  if cmdArg == "rotate":
    img = makePicture(pickAFile())
    canvas = makeEmptyPicture((getHeight(img)*2),(getWidth(img)*2), blue)
    rotateFn(img,canvas,sPath)
  elif cmdArg == "flip":
    img = makePicture(pickAFile())
    canvas = makeEmptyPicture((getHeight(img)*2),(getWidth(img)*2), blue)
    flipFn(img,canvas,sPath)
  else:
    print "You must have 'flip' or 'rotate' as your first command line argument"
    
def rotateFn(img,canvas,sPath):
  print "you selected rotate"
  
  rotatingFn(img,canvas)
  mirrorHorizontal(canvas)
  mirrorVertical(canvas)
  explore(canvas)
  writePictureTo(canvas,sPath)

def rotatingFn(img,canvas):
  targetX =0
  width = getWidth(img)
  for srcX in range(0,width):
    targetY = 0 
    for srcY in range(0,getHeight(img)):
      color = getColor(getPixel(img,srcX,srcY))
      setColor(getPixel(canvas,targetY,width - targetX -1),color)
      targetY = targetY + 1
    targetX = targetX + 1

def rotateFlipFn(img,canvas): #prog 80 in book
  targetX = 0
  for srcX in range(0,getWidth(img)):
    targetY = 0
    for srcY in range(0,getHeight(img)):
      color = getColor(getPixel(img,srcX,srcY))
      setColor(getPixel(canvas,targetY,targetX), color)
      targetY = targetY + 1
    targetX = targetX + 1

def mirrorHorizontal(canvas):
  mirrorPt = getHeight(canvas)/2
  height = getHeight(canvas)
  for x in range(0,getWidth(canvas)):
    for y in range(0, mirrorPt):
      topPxl = getPixel(canvas,x,y)
      bottomPxl = getPixel(canvas,x, height-y-1)
      color = getColor(topPxl)
      setColor(bottomPxl,color)

def mirrorVertical(canvas):
  mirrorPt = getWidth(canvas)/2
  width = getWidth(canvas)
  for y in range(0,getHeight(canvas)):
    for x in range(0,mirrorPt):
      topPxl = getPixel(canvas,x,y)
      bottomPxl = getPixel(canvas,width-x-1, y)
      color = getColor(topPxl)
      setColor(bottomPxl,color)

def flipFn(img,canvas,sPath):
  print "you flipped"
  
  rotateFlipFn(img,canvas)
  mirrorHorizontal(canvas)
  mirrorVertical(canvas)
  explore(canvas)
  writePictureTo(canvas,sPath)