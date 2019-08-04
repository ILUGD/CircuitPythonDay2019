import time
import array
import math
import audioio
import board
import digitalio
import random
import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    FREQUENCY = random.randint(20,4000)
    SAMPLERATE = 8000

    color = FREQUENCY%256
    led[0] = (color, 0, 0)
    led[1] = (color, 256-color, 0)
    led[2] = (0, 0, color)
    led[3] = (color, color, 256-color)
    led[4] = (256-color, color, 256-color)
    led[5] = (0,0,color)
    led[6] = (color, 50, 256-color)

    length = SAMPLERATE // FREQUENCY
    sine_wave = array.array("H", [0] * length)
    for i in range(length):
        sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15)

    # enable the speaker
    speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
    speaker_enable.direction = digitalio.Direction.OUTPUT
    speaker_enable.value = True

    audio = audioio.AudioOut(board.A0)
    sine_wave_sample = audioio.RawSample(sine_wave)

    audio.play(sine_wave_sample, loop=True)
    time.sleep(1)
    audio.stop()