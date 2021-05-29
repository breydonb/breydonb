import random
def mainFn():
  img = makePicture(r"C:\Users\B226-05\Desktop\fordgt25pct.jpg")
  world = makeEmptyPicture(1000,1000,blue)
  turtle = makeTurtle(world)
  #dropFn(world,turtle,img)
  #drop2Fn(world,turtle,img)
  drop3Fn(world,turtle,img)
  explore(world)
  #writePictureTo(world,r"C:\Users\B226-05\Desktop\test\test3.jpg")
def dropFn(world,turtle,img):
  for i in range(12):
    turtle.drop(img)
    turtle.forward(10)
    turtle.turn(-30)
    
def drop2Fn(world,turtle,img):
  turtle.penUp()
  turtle.backward(getWidth(world))
  for i in range(12):
    turtle.drop(img)
    turtle.forward(100)
    turtle.turn(20)
  
  for i in range(100):
    turtle.penDown()
    turtle.drop(img)
    turtle.forward(10)
    turtle.penUp()
    
def drop3Fn(world,turtle,img):
  for i in range(36):
    turtle.penDown()
    turtle.drop(img)
    turtle.penUp()
    turtle.forward(100)
    turtle.turn(10)
    