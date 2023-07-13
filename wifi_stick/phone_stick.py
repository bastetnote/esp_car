import socket
# import wifi_connect


def socket_udp_server(server_ip: str = '0.0.0.0', server_port: int = 9999, buffer_size: int = 1024):
    """
    socket udp server

    :param server_ip: default 0.0.0.0, allow all
    :param server_port: default 9999
    :param buffer_size: default 1024
    :return: none
    """
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((server_ip, server_port))
    print('Server listening')
    return udp_socket

def receive_stick_str(udp_socket, buffer_size: int = 1024):
    receive_data, sender_info = udp_socket.recvfrom(buffer_size)
    udp_str = ('00' + receive_data.decode('utf-8'))[-8:]    # same as zfill
    print('Client info ', sender_info)
    print('Client data ', udp_str)
    return udp_str
#         left_stick_x = int(stick_str[0:2])-16
#         left_stick_y = int(stick_str[2:4])-16
#         right_stick_x = int(stick_str[4:6])-16
#         right_stick_y = int(stick_str[6:8])-16
#         print(left_stick_x, left_stick_y, right_stick_x, right_stick_y)
        

# if __name__ == '__main__':
#     ssid = 'mpy-ap'
#     password = '12345678'
#     ip = '192.168.178.1'
#     ip = wifi_connect.create_accesspoint(ssid, password, ip)
#     socket_udp_server()