def mainFn():
  world = makeWorld()
  turtle = makeTurtle(world)
  drawCircle(turtle,100)
  
  
def drawCircle(turtle,width):
  turtle.setPenWidth(4)
  for i in range(0,360):
    turtle.penUp()
    turtle.forward(width)
    turtle.penDown()
    turtle.forward(1)
    turtle.penUp()
    turtle.turn(180)
    turtle.forward(width)
    turtle.turn(1)