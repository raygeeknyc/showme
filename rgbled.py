import RPi.GPIO as GPIO

# Pin Definitons:
redPin = 2
greenPin = 3
bluePin = 4

class RgbLed:
    GPIO.setmode(GPIO. BOARD)

    RED = (True, False, False)
    GREEN = (False, True, False)
    BLUE = (False, False, True)
    WHITE = (True, True, True)
    YELLOW = (True, True, False)
    CYAN = (False, True, True)
    MAGENTA = (True, False, True)
    OFF = (False, False, False)

    def __init__(self, redPin, GreenPin, BluePin):

        self._redPin = redPin
        self._GreenPin = GreenPin
        self._BluePin = BluePin

        GPIO.setup(self._redPin, GPIO.OUT)
        GPIO.setup(self._greenPin, GPIO.OUT)
        GPIO.setup(self._bluePin, GPIO.OUT)
        self.setColor(RgbLed.OFF)

    def setColor(rgb):
        GPIO.output(self._redPin, (rgb[0])?GPIO.LOW:GPIO.HIGH)
        GPIO.output(self._greenPin, (rgb[1])?GPIO.LOW:GPIO.HIGH) 
        GPIO.output(self._bluePin, (rgb[2])?GPIO.LOW:GPIO.HIGH)

if __name__ == "__main__":
    demo = RgbLed(redPin, greenPin, bluePin)
    demo.setColor(RgbLed.RED)
    time.sleep(1)
    demo.setColor(RgbLed.GREEN)
    time.sleep(1)
    demo.setColor(RgbLed.BLUE)
    time.sleep(1)
    demo.setColor(RgbLed.OFF)
    time.sleep(2)
    demo.setColor(RgbLed.CYAN)
    time.sleep(1)
    demo.setColor(RgbLed.YELLOW)
    time.sleep(1)
    demo.setColor(RgbLed.MAGENTA)
    time.sleep(1)
    demo.setColor(RgbLed.WHITE)
    time.sleep(1)
