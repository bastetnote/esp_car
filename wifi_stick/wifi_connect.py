import network


def create_accesspoint(ssid, pwd, ip=''):
    """
    ESP32 as Accesspoint

    :param ssid
    :param pwd
    :param ip
    :return: ip
    """
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, authmode=network.AUTH_WPA_WPA2_PSK, password=pwd)
    if len(ip) > 0:
        ip_info = (ip, '255.255.255.0', ip, '8.8.8.8')
        ap.ifconfig(ip_info)
        print('Setting ip_info ', ip_info)
    while ap.active() == False:
        pass
    
    ip_info = ap.ifconfig()
    print('Accesspoint ready ', ip_info)
    return ip_info[0]


def connect_wifi(ssid, pwd, ip=''):
    """
    Connect to existing Wifi

    :param ssid
    :param pwd
    :param ip
    :return: ip
    """
    mynet = network.WLAN(network.STA_IF)
    if not mynet.isconnected():
        mynet.active(True)
        mynet.connect(ssid, pwd)
    if len(ip) > 0:
        ip_info = (ip, '255.255.255.0', ip, '8.8.8.8')
        mynet.ifconfig(ip_info)
        print('Setting ip_info ', ip_info)
    ip = mynet.ifconfig()[0]
    return ip

if __name__ == '__main__':
    ssid = 'Mi10w'
    password = '1234567a'
#     ip = '192.168.178.1'
    ip = connect_wifi(ssid, password, '')