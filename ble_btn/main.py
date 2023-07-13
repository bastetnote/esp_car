import bluetooth
from machine import Pin
from ble_uart_peripheral import BLEUART
from mecanum import MECANUM


# LED = Pin(2, Pin.OUT)

def car_ble_controller():
    ble = bluetooth.BLE()
    uart = BLEUART(ble, name='mpy-car')
    
    #bluetooth rx callback ：蓝牙接受回调函数
    def on_rx():
        data = uart.read()
        print(data)
        # ↖A41 ↑G47 ↗C43
        # ← H48 停I49 →J4A
        # ↙D44 ↓K4B ↘F46
        # 顺B42 逆E45        
        
        if len(data) > 0:
            if data == b'I' or data == b'\xa5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Z':
                car.stop()
#                 uart.write('Car stop', notify=False) # 蓝牙发送消息到主机且通知
            elif data == b'G' or data == b'\xa5\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01Z':                 
                car.forward()
            elif data == b'K' or data == b'\xa5\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x02Z':     
                car.backward()
            elif data == b'H' or data == b'\xa5\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x03Z':  
                car.left()
            elif data == b'J' or data == b'\xa5\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x04Z':    
                car.right()
            elif data == b'A' or data == b'\xa5\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05Z':   
                car.front_left()
            elif data == b'C' or data == b'\xa5\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x06Z':     
                car.front_right()
            elif data == b'D' or data == b'\xa5\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x07Z':
                car.back_left()
            elif data == b'F' or data == b'\xa5\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x08Z':
                car.back_right()
            elif data == b'B' or data == b'\xa5\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\tZ':
                car.clockwise()
            elif data == b'E' or data == b'\xa5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\nZ':
                car.counterclockwise()
            else:
                car.stop()
            
    uart.irq(handler=on_rx)
    uart.close()
            
  
if __name__ == '__main__':
    car = MECANUM()
    car.stop()
    car_ble_controller()
    
