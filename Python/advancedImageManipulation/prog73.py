def mainFn():
  img = makePicture(r"C:\Users\B226-05\Desktop\gt25pct.jpg")
  canvas = makeEmptyPicture(getWidth(img)*2, getHeight(img)*2, green)
  
  writeFn(canvas,img,0,0)
  writeFn(canvas,img,0,getHeight(img))
  writeFn(canvas,img,getWidth(img),0)
  writeFn(canvas,img,getWidth(img),getHeight(img))
  
  copyFriend(img,canvas)
  
  explore(canvas)

  
  
  
def copyFriend(img,canvas):
  for i in [200,407,814,1221]:    #Spaced evenish is 200,407,814,1221
    targetX=0 #this controls the width on the blank canvas
    targetX=targetX+int(i)
    for sourceX in range(532,588):
      targetY=(80)  #this controls the height on the blank canvas
      for sourceY in range(28,120):
        color=getColor(getPixel(img,sourceX,sourceY))
        setColor(getPixel(canvas,targetX,targetY),color)
        targetY=targetY+1
      targetX=targetX+1
      
def writeFn(canvas,img,startX,startY):
  targetX=startX
  for x in range(0, getWidth(img)):
    targetY= startY
    for y in range(0,getHeight(img)):
      color=getColor(getPixel(img,x,y))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY+1
    targetX= targetX+1