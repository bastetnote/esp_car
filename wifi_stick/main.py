import wifi_connect
import phone_stick
import motor_speed


if __name__ == '__main__':
    ssid = 'Xiaomi_010040'
    password = '8613564309393'
    #ip = '192.168.178.1'
    #ip = wifi_connect.create_accesspoint(ssid, password, ip)
    
    ip = wifi_connect.connect_wifi(ssid, password, '')
    udp_socket = phone_stick.socket_udp_server()
    
    while True:
#         try:
        udp_str = phone_stick.receive_stick_str(udp_socket)
        if len(udp_str) > 0:
            wheel_speed = motor_speed.calculate_wheel_speed(udp_str)
            motor_speed.mecanum_run(wheel_speed)
#         except KeyboardInterrupt:
#                 motor_speed.mecanum_run([0,0,0,0])
    
    