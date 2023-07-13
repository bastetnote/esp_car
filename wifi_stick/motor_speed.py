from machine import Pin, PWM

MAX_SPEED = 1000

class Motor:
    def __init__(self, in_p, in_n):
        self.in_p = PWM(Pin(in_p), freq=100, duty=0)
        self.in_n = PWM(Pin(in_n), freq=100, duty=0)

    def set_speed(self, v):
        if v > 0:
          self.in_p.duty(v)
          self.in_n.duty(0)
        elif v < 0:
          self.in_p.duty(0)
          self.in_n.duty(-v)
        else:
          self.in_p.duty(0)
          self.in_n.duty(0)

# FL FR BR BL
motor = [Motor(15,0), Motor(4,16), Motor(17,5), Motor(18,19)]


def scale_up(x, in_min, in_max, out_min, out_max):    # same as Arduino map
    if in_min != in_max:
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    else:
        return max(min(x, out_max), out_min)


def calculate_wheel_speed(udp_str):
    stick_int = [int(udp_str[i:i+2]) - 16 for i in range(0, len(udp_str), 2)]    # udp_str 0~32; stick_int -16 ~ 16
    stick_int[2] = int(stick_int[2] / 2)
    
    # FL FR BR BL wheel speed
    speed = [0,0,0,0]
    speed[0] = -stick_int[1] + stick_int[0] + stick_int[2]
    speed[1] = -stick_int[1] - stick_int[0] - stick_int[2]
    speed[2] = -stick_int[1] + stick_int[0] - stick_int[2]
    speed[3] = -stick_int[1] - stick_int[0] + stick_int[2]

#     speed[0] = -stick_int[1] + int(stick_int[0]*1.1) + stick_int[2]
#     speed[1] = -stick_int[1] - int(stick_int[0]*1.1) - stick_int[2]
#     speed[2] = -stick_int[1] + int(stick_int[0]*1.1) - stick_int[2]
#     speed[3] = -stick_int[1] - int(stick_int[0]*1.1) + stick_int[2]

    # normalize
    print('Before normalized ', speed)    
    maxMagnitude = max(abs(x) for x in speed)
    wheel_speed = list(map(lambda x:scale_up(x, -maxMagnitude, maxMagnitude, -MAX_SPEED, MAX_SPEED), speed))    
    print('After normalized ', wheel_speed)
    
    # 2
#     print('Before normalized ', speed)
#     maxMagnitude = max(abs(stick_int[1]) + abs(int(stick_int[0]*1.1)) + abs(stick_int[2]), 1)
#     wheel_speed = list(map(lambda x:scale_up(x, -maxMagnitude, maxMagnitude, -MAX_SPEED, MAX_SPEED), speed))    
#     print('After normalized ', wheel_speed)
    
    
    return wheel_speed

def mecanum_run(wheel_speed):    
    for i in range(4):
        motor[i].set_speed(wheel_speed[i])       




# if __name__ == '__main__':
#     
#     udp_data = '00161616'
#     mecanum_move(udp_data)
    
