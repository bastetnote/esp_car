from machine import Pin, PWM
import time

class MECANUM():    
    def __init__(self):
        # FL12-------FR34
        #
        #
        # BL78-------BR56

        # front left motor
        self.FL_P = PWM(Pin(15), freq=100, duty=0)
        self.FL_N = PWM(Pin(0), freq=100, duty=0)
 
        # front right motor
        self.FR_P = PWM(Pin(4), freq=100, duty=0)
        self.FR_N = PWM(Pin(16), freq=100, duty=0)

        # back right motor
        self.BR_P = PWM(Pin(17), freq=100, duty=0)
        self.BR_N = PWM(Pin(5), freq=100, duty=0)

        # back left motor
        self.BL_P = PWM(Pin(18), freq=100, duty=0)
        self.BL_N = PWM(Pin(19), freq=100, duty=0)

        # motor speed, default maximum
        self.duty = 500
        
    # Mecanum wheel
    def stop(self):
        self.FL_P.duty(0)
        self.FL_N.duty(0)
        self.FR_P.duty(0)
        self.FR_N.duty(0)
        self.BR_P.duty(0)
        self.BR_N.duty(0)
        self.BL_P.duty(0)
        self.BL_N.duty(0)
    
    def forward(self):
        speed = self.duty
        self.FL_P.duty(speed)
        self.FL_N.duty(0)
        self.FR_P.duty(speed)
        self.FR_N.duty(0)
        self.BR_P.duty(speed)
        self.BR_N.duty(0)
        self.BL_P.duty(speed)
        self.BL_N.duty(0)
    
    def backward(self):
        speed = self.duty
        self.FL_P.duty(0)
        self.FL_N.duty(speed)
        self.FR_P.duty(0)
        self.FR_N.duty(speed)
        self.BR_P.duty(0)
        self.BR_N.duty(speed)
        self.BL_P.duty(0)
        self.BL_N.duty(speed)
        
    def left(self):
        speed = self.duty
        self.FL_P.duty(0)
        self.FL_N.duty(speed)
        self.FR_P.duty(speed)
        self.FR_N.duty(0)
        self.BR_P.duty(0)
        self.BR_N.duty(speed)
        self.BL_P.duty(speed)
        self.BL_N.duty(0)
        
    def right(self):
        speed = self.duty
        self.FL_P.duty(speed)
        self.FL_N.duty(0)
        self.FR_P.duty(0)
        self.FR_N.duty(speed)
        self.BR_P.duty(speed)
        self.BR_N.duty(0)
        self.BL_P.duty(0)
        self.BL_N.duty(speed)
        
    def front_left(self):
        speed = self.duty
        self.FL_P.duty(0)
        self.FL_N.duty(0)
        self.FR_P.duty(speed)
        self.FR_N.duty(0)
        self.BR_P.duty(0)
        self.BR_N.duty(0)
        self.BL_P.duty(speed)
        self.BL_N.duty(0)
        
    def front_right(self):
        speed = self.duty
        self.FL_P.duty(speed)
        self.FL_N.duty(0)
        self.FR_P.duty(0)
        self.FR_N.duty(0)
        self.BR_P.duty(speed)
        self.BR_N.duty(0)
        self.BL_P.duty(0)
        self.BL_N.duty(0)

    def back_left(self):
        speed = self.duty
        self.FL_P.duty(0)
        self.FL_N.duty(speed)
        self.FR_P.duty(0)
        self.FR_N.duty(0)
        self.BR_P.duty(0)
        self.BR_N.duty(speed)
        self.BL_P.duty(0)
        self.BL_N.duty(0)
        
    def back_right(self):
        speed = self.duty
        self.FL_P.duty(0)
        self.FL_N.duty(0)
        self.FR_P.duty(0)
        self.FR_N.duty(speed)
        self.BR_P.duty(0)
        self.BR_N.duty(0)
        self.BL_P.duty(0)
        self.BL_N.duty(speed)
        
    def clockwise(self):
        speed = self.duty
        self.FL_P.duty(speed)
        self.FL_N.duty(0)
        self.FR_P.duty(0)
        self.FR_N.duty(speed)
        self.BR_P.duty(0)
        self.BR_N.duty(speed)
        self.BL_P.duty(speed)
        self.BL_N.duty(0) 
        
    def counterclockwise(self):
        speed = self.duty
        self.FL_P.duty(0)
        self.FL_N.duty(speed)
        self.FR_P.duty(speed)
        self.FR_N.duty(0)
        self.BR_P.duty(speed)
        self.BR_N.duty(0)
        self.BL_P.duty(0)
        self.BL_N.duty(speed)


car = MECANUM()
time.sleep_ms(1000)

car.forward()
time.sleep(0.5)
car.stop()
#      
# car.back()
# time.sleep(0.5)
# car.stop()

# car.left()
# time.sleep(0.5)
# car.stop()
# 
# car.right()
# time.sleep(0.5)
# car.stop()

# car.front_left()
# time.sleep(0.5)
# car.stop()
# 
# car.front_right()
# time.sleep(0.5)
# car.stop()
# 
# car.back_left()
# time.sleep(0.5)
# car.stop()
# 
# car.back_right()
# time.sleep(0.5)
# car.stop()
# 
# car.clockwise()
# time.sleep(0.5)
# car.stop()
# 
# car.counterclockwise()
# time.sleep(0.5)
# car.stop()
