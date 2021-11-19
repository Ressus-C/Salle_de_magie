import GPIO
import time
import Websockets
import sys

if __name__ == '__main__':
    MonGPIO = GPIO.Mygpio()
    MonGPIO.Write(14, 0)
    print("Python version")
    print(sys.version)
    print("Version info.")
    print(sys.version_info)
    for plop in range(0, 28):
        valeur = MonGPIO.Read(plop)
        print(plop, " = ", valeur)
    while 1:
        if MonGPIO.wait(2):
            print("plaf")
        """time.sleep(1)"""
