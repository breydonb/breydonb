def mainFn(numArg,sName):
  print "Pick your directory"
  sPath = setMediaPath()
  for i in range(1,10):
    img1 = makePicture(sPath + str(i)+ ".jpg")
    img2 = makePicture(sPath + str(i)+ ".jpg")
    img3 = makePicture(sPath + str(i)+ ".jpg")
    img4 = makePicture(sPath + str(i)+ ".jpg")
    img5 = makePicture(sPath + str(i)+ ".jpg")
    img6 = makePicture(sPath + str(i)+ ".jpg")
    img7 = makePicture(sPath + str(i)+ ".jpg")
    img8 = makePicture(sPath + str(i)+ ".jpg")
    img9 = makePicture(sPath + str(i)+ ".jpg")
    
  if numArg == 4:
    canvas = makeEmptyPicture(getWidth(img1)*2, getHeight(img1)*2)
    writeMulti(img1,canvas,0,0)
    writeMulti(img2,canvas,0,getHeight(img1))
    writeMulti(img3,canvas,getWidth(img1),0)
    writeMulti(img4,canvas,getWidth(img1),getHeight(img1))
    explore(canvas)
    
  elif numArg == 9:
    canvas = makeEmptyPicture(getWidth(img1)*3, getHeight(img1)*3)
    writeMulti(img1,canvas,0,0)
    writeMulti(img2,canvas,getWidth(img1),0)
    writeMulti(img2,canvas,getWidth(img1)*2,0)
    
    writeMulti(img3,canvas,getWidth(img1),getHeight(img1))
    writeMulti(img4,canvas,0,getHeight(img1))    
    writeMulti(img3,canvas,getWidth(img1)*2,getHeight(img1))
    
    writeMulti(img3,canvas,getWidth(img1),getHeight(img1)*2)
    writeMulti(img3,canvas,0,getHeight(img1)*2)
    writeMulti(img3,canvas,getWidth(img1)*2,getHeight(img1)*2)
    explore(canvas)
    
def writeMulti(img,canvas,targetX,sentY):
  for srcX in range(0,getWidth(img)):
    targetY = sentY
    for srcY in range(0, getHeight(img)):
      color = getColor(getPixel(img,srcX,srcY))
      setColor(getPixel(canvas,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1