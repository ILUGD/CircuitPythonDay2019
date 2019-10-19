import time
import pulseio
import board
import adafruit_irremote
from adafruit_circuitplayground.express import cpx

cpx.pixels.fill((20,255,20))
cpx.pixels.brightness = 0.5
health = 10
hits = 0

# Create a 'pulseio' input, to listen to infrared signals on the IR receiver
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
# Create a decoder that will take pulses and turn them into numbers
decoder = adafruit_irremote.GenericDecode()

pwm = pulseio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulseout = pulseio.PulseOut(pwm)
# Create an encoder that will take numbers and turn them into NEC IR pulses
encoder = adafruit_irremote.GenericTransmit(header=[9500, 4500], one=[550, 550],
                                            zero=[550, 1700], trail=0)

while True:
    if cpx.button_a or cpx.button_b:
        print("\nTrigger pressed! \n")
        cpx.red_led = True
        encoder.transmit(pulseout, [66, 84, 78, 65])
        cpx.play_file("gun.wav")
        cpx.red_led = False
        # wait so the receiver can get the full message
        time.sleep(0.1)
        #pulsein.clear()
        
    pulses = decoder.read_pulses(pulsein)
    pulsein.clear()
    try:
        # Attempt to convert received pulses into numbers
        received_code = decoder.decode_bits(pulses, debug=False)
    except adafruit_irremote.IRNECRepeatException:
        # We got an unusual short code, probably a 'repeat' signal
        continue
    except adafruit_irremote.IRDecodeException:
        # Something got distorted
        continue
    if received_code == [66, 84, 78, 65]:
        health -=1
        hits +=1
        cpx.pixels[health] = (255,0,0)
        print("Got a hit! ")
        print("Health left: " +str(health))
        if(health == 0):
            break
        
print("You died!")
cpx.play_file("die.wav")
while True:
    cpx.pixels.brightness = 0.25
    for i in range(10):
        cpx.pixels.fill((100-i*5,100-i*5,255-i*10))
        cpx.pixels.brightness = 0.10
        time.sleep(0.10)
    
