# Write your code here :-)
from adafruit_circuitplayground.express import cpx
from time import sleep
cpx.pixels.brightness=.3
while True:
  x,y,z = cpx.acceleration
  print((x, y, z))
  sleep(.2)

  if y <10 and y>7 :
      cpx.pixels[3] = (120, 2, 90)
      cpx.pixels[4] = (120, 2, 90)
      cpx.pixels[5] = (120, 2, 90)
      cpx.pixels[6] = (120, 2, 90)
      cpx.pixels[1] = (0,0,0)
      cpx.pixels[2] = (0,0,0)
      cpx.pixels[7] = (0,0,0)
      cpx.pixels[8] = (0,0,0)
      cpx.pixels[9] = (0,0,0)
      cpx.pixels[0] = (0,0,0)

  if y < 5  and y>1 :
      cpx.pixels[3] = (120, 2, 90)
      cpx.pixels[4] = (120, 2, 90)
      cpx.pixels[5] = (120, 2, 90)
      cpx.pixels[2] = (120, 2, 90)
      cpx.pixels[1] = (0,0,0)
      cpx.pixels[6] = (0,0,0)
      cpx.pixels[7] = (0,0,0)
      cpx.pixels[8] = (0,0,0)
      cpx.pixels[9] = (0,0,0)
      cpx.pixels[0] = (0,0,0)

  if y < 0 and y>-2 :

      cpx.pixels[3] = (120, 2, 90)
      cpx.pixels[4] = (120, 2, 90)
      cpx.pixels[2] = (120, 2, 90)
      cpx.pixels[1] = (120, 2, 90)
      cpx.pixels[5] = (0,0,0)
      cpx.pixels[6] = (0,0,0)
      cpx.pixels[7] = (0,0,0)
      cpx.pixels[8] = (0,0,0)
      cpx.pixels[9] = (0,0,0)
      cpx.pixels[0] = (0,0,0)
  if y < -4 and y>-8 :

      cpx.pixels[3] = (120, 2, 90)
      cpx.pixels[0] = (120, 2, 90)
      cpx.pixels[2] = (120, 2, 90)
      cpx.pixels[1] = (120, 2, 90)
      cpx.pixels[5] = (0,0,0)
      cpx.pixels[6] = (0,0,0)
      cpx.pixels[7] = (0,0,0)
      cpx.pixels[8] = (0,0,0)
      cpx.pixels[9] = (0,0,0)
      cpx.pixels[4] =(0,0,0)



