import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and s$
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
print("Digite 8 para frente ou 2 para tras ou 4 para esquerda ou 6 para direita ou 5 para parar")

def frente():
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
def tras():
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
        GPIO.output(8, GPIO.HIGH)
def direita():
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
def esquerda():
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)
        GPIO.output(8, GPIO.LOW)
def pare():
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
        GPIO.output(8, GPIO.LOW)

while True: # Run forever
        try:
                d=input()
                if d==8:
                        frente()
                elif d==2:
                        tras()
                elif d==4:
                        esquerda()
                elif d==6:
                        direita()
                elif d==5:
                        pare()
        except:
                print("Voce so poderia ter digitado 8 ou 2 ou 4 ou 6 ou 5")


