from machine import Pin, SoftI2C, PWM
from I2C_LCD import I2cLcd
from neopixel import NeoPixel
from random import randint
from time import sleep, sleep_ms

# -------------------
# BEEP FUNCTION
# -------------------

def beep():
    buzzer = PWM(Pin(15))
    buzzer.freq(3000)
    buzzer.duty_u16(50000)
    sleep_ms(40)
    buzzer.duty_u16(0)
    buzzer.deinit()

# -------------------
# PIN SETUP
# -------------------

NUM_LEDS = 35

LED_PIN = 7
TAKKI_PIN = 11
REED_PIN = 9

np = NeoPixel(Pin(LED_PIN), NUM_LEDS)

takki = Pin(TAKKI_PIN, Pin.IN, Pin.PULL_UP)
reed = Pin(REED_PIN, Pin.IN, Pin.PULL_UP)

i2c = SoftI2C(scl=Pin(6), sda=Pin(5), freq=100000)
lcd = I2cLcd(i2c, 39, 2, 16)

# RGB strip (þinn kóði)
RGBLP = NeoPixel(Pin(13), 9)

# -------------------
# START
# -------------------

lcd.clear()
game_over = False

# -------------------
# MAIN LOOP
# -------------------

while True:


    RGBLP[0] = (0, 0, 150)
    RGBLP[1] = (0, 150, 0)
    RGBLP[2] = (0, 150, 0)
    RGBLP[3] = (0, 0, 150)
    RGBLP[4] = (0, 150, 0)
    RGBLP[5] = (0, 0, 150)
    RGBLP[6] = (0, 0, 150)
    RGBLP[7] = (0, 0, 150)
    RGBLP[8] = (0, 150, 0)

    RGBLP.write()

    # -------- BUTTON --------
    if takki.value() == 0:

        sleep_ms(200)

        # 3 hringir
        for _ in range(3):
            for i in range(NUM_LEDS):
                np.fill((0, 0, 0))
                np[i] = (200, 200, 200)
                np.write()
                sleep_ms(10)

        np.fill((0, 0, 0))
        np.write()

        # Teningur
        dice = randint(1, 6)

        # 🔊 EINN STUTT PÍP
        beep()

        lcd.clear()
        lcd.putstr(str(dice))

        sleep(2)
        lcd.clear()

    # -------- REED --------
    if reed.value() == 0 and not game_over:
        game_over = True
        lcd.clear()
        lcd.putstr("YAYY")
        sleep(3)
        lcd.clear()

    sleep_ms(100)