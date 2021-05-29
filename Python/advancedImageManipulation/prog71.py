def mainFn():
  img = makePicture(r"C:\Users\B226-05\Desktop\gt25pct.jpg")
  canvas = makeEmptyPicture(getWidth(img)*2,getHeight(img)*2,blue)
  writeFn(canvas,img,0,0)  
  writeFn(canvas,img,getWidth(img),getHeight(img)) #You must make another function in order to print a different 
  writeFn(canvas,img,0,getHeight(img))
  
  explore(canvas)
  
def writeFn(canvas,img,startX,startY):
  targetX=startX
  for x in range(0, getWidth(img)):
    targetY= startY
    for y in range(0,getHeight(img)):
      color=getColor(getPixel(img,x,y))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY+1
    targetX= targetX+1