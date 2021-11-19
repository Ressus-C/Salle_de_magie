import RPi.GPIO as GPIO


class Mygpio:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for channel in range(0, 12):
            GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(0, GPIO.IN)
        GPIO.setup(1, GPIO.IN)
        GPIO.setup(2, GPIO.IN)
        GPIO.setup(3, GPIO.IN)
        GPIO.setup(4, GPIO.IN)
        GPIO.setup(5, GPIO.IN)
        GPIO.setup(6, GPIO.IN)
        GPIO.setup(7, GPIO.IN)
        GPIO.setup(8, GPIO.IN)
        GPIO.setup(9, GPIO.IN)
        GPIO.setup(10, GPIO.IN)
        GPIO.setup(11, GPIO.IN)
        GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(14, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(15, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(19, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(20, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(21, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(23, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(25, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH)

    def Read(self, numGPIO):
        return GPIO.input(numGPIO)

    def Write(self, numGPIO, value):
        if value == 0:
            print(numGPIO, value)
            GPIO.output(numGPIO, GPIO.LOW)
        if value == 1:
            print(numGPIO, value)
            GPIO.output(numGPIO, GPIO.HIGH)

    def wait(self, numGPIO):
        return GPIO.wait_for_edge(numGPIO, GPIO.FALLING)


if __name__ == '__main__':
    MonGPIO = Mygpio()
    MonGPIO.Write(14, 0)
    for plop in range(0, 28):
        valeur = MonGPIO.Read(plop)
        print(plop, " = ", valeur)
