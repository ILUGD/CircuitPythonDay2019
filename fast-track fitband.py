from time import sleep
import board

from adafruit_circuitplayground.express import cpx

prev, res, total = 0, 0, 0
while True:

  x, y, z = cpx.acceleration
  sleep(2)
  total = abs(abs(x) - prev)
  prev = abs(x)
  res = res + total
  print(res)
  if res >= 2:
    cpx.pixels[0] = (255 , 0 , 0)
  if res >=4:
    cpx.pixels[1] = (0 , 255 , 0)
  if res >=6:
    cpx.pixels[2] = (0 , 0 , 255)
  if res >= 8:
    cpx.pixels[3] = (255 , 0 , 0)
  if res >=10:
    cpx.pixels[4] = (0 , 255 , 0)
  if res >=12:
    cpx.pixels[5] = (0 , 0 , 255)
  if res >=14:
    cpx.pixels[6] = (255 , 0 , 0)
  if res >=16:
    cpx.pixels[7] = (0 , 255 , 0)
  if res >=18:
    cpx.pixels[8] = (0 , 0 , 255)
  if res >= 20:
    cpx.pixels[9] = (255 , 0 , 0)
    cpx.start_tone(523)
