import time
import RPi.GPIO as GPIO
import threading
import sys

# Pin Definitons:
redPin = 2
greenPin = 3
bluePin = 4

class RgbLed:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    RED = (True, False, False)
    GREEN = (False, True, False)
    BLUE = (False, False, True)
    WHITE = (True, True, True)
    YELLOW = (True, True, False)
    CYAN = (False, True, True)
    MAGENTA = (True, False, True)
    OFF = (False, False, False)

    def __init__(self, redPin, greenPin, bluePin):

        self._redPin = redPin
        self._greenPin = greenPin
        self._bluePin = bluePin

        GPIO.setup(self._redPin, GPIO.OUT)
        GPIO.setup(self._greenPin, GPIO.OUT)
        GPIO.setup(self._bluePin, GPIO.OUT)
        self.setColor(RgbLed.OFF)

    def setColor(self, rgb):
        self._color = rgb
        GPIO.output(self._redPin, GPIO.LOW if rgb[0] else GPIO.HIGH)
        GPIO.output(self._greenPin, GPIO.LOW if rgb[1] else GPIO.HIGH)
        GPIO.output(self._bluePin, GPIO.LOW if rgb[2] else GPIO.HIGH)

    def stop(self):
        self._stop = True

    def cycle(self, interval_secs):
        self._interval_secs = interval_secs
        self.setColor(RgbLed.RED)
        self._stop = False
        while not self._stop:
            time.sleep(self._interval_secs)
            self._cycleColor()

    def _cycleColor(self):
        if self._color is RgbLed.RED:
            self.setColor(RgbLed.GREEN)
        elif self._color is RgbLed.GREEN:
            self.setColor(RgbLed.BLUE)
        elif self._color is RgbLed.BLUE:
            self.setColor(RgbLed.CYAN)
        elif self._color is RgbLed.CYAN:
            self.setColor(RgbLed.YELLOW)
        elif self._color is RgbLed.YELLOW:
            self.setColor(RgbLed.WHITE)
        elif self._color is RgbLed.WHITE:
            self.setColor(RgbLed.OFF)
        elif self._color is RgbLed.OFF:
            self.setColor(RgbLed.RED)

if __name__ == "__main__":
    demo = RgbLed(redPin, greenPin, bluePin)
    demo.setColor(RgbLed.RED)
    time.sleep((0.5))
    demo.setColor(RgbLed.GREEN)
    time.sleep((0.5))
    demo.setColor(RgbLed.BLUE)
    time.sleep((0.5))
    demo.setColor(RgbLed.OFF)
    time.sleep(2)
    demo.setColor(RgbLed.CYAN)
    time.sleep((0.5))
    demo.setColor(RgbLed.YELLOW)
    time.sleep((0.5))
    demo.setColor(RgbLed.MAGENTA)
    time.sleep((0.5))
    demo.setColor(RgbLed.WHITE)
    time.sleep((0.5))
    demo.setColor(RgbLed.OFF)

    sleepLed = threading.Thread(target = demo.cycle, args=(2,))
    sleepLed.start()
    response = raw_input("waiting for you before stopping... ")
    demo.stop()
    print "waiting for LED to stop cycling"
    sleepLed.join()
    GPIO.cleanup()
    sys.exit()
