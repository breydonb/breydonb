def mainFn(scaleArg):
  img= makePicture(r"C:\Users\B226-05\Desktop\buffalos.jpg")
  
  canvas = makeEmptyPicture(getWidth(img)/scaleArg,getHeight(img)/scaleArg)
  
  scaleImg(img,canvas,scaleArg)
  
  explore(canvas)
  
def scaleImg(img,canvas,scaleArg):
  sourceX = 0
  for targetX in range(0, int(getWidth(img)/scaleArg)):
    sourceY = 0
    for targetY in range(0, int(getHeight(img)/scaleArg)):
      color = getColor(getPixel(img,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY),color)
      sourceY = sourceY + 2
    sourceX = sourceX + 2
    