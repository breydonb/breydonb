def mainFn():
  world = makeWorld()
  turtle = makeTurtle(world)
  squareFn(turtle,world)
  
def squareFn(turtle,world):
  for i in range(1,1000):
    x = randint(1, 100)
    turtle.turnRight()
    turtle.forward(x)
    iRed= randint(0,255)
    iGreen = randint(0,255)
    iBlue = randint(0,255)
    
    turtle.setPenColor(makeColor(iRed,iGreen,iBlue))
