#!/usr/bin/env python3

# using it to find rockpis ip

import socket
import json
import sys
import mylogger as log
from functools import wraps


PORT = 37020

logger = log.init_logger()  # __name__, testing_mode=True)


def decorate_broadcast(func):
    @wraps(func)
    def wrapper(a):
        address = func(a)
        logger.debug("Broadcast: " + address)
        return address

    return wrapper


@decorate_broadcast
def set_broadcast_address(arg):
    """set broadcast address

    :param arg: 'dev' or any other
    :type arg: string
    :return: ip address
    :rtype: string 
    """
    if arg == 'dev':
        b = '192.168.4.255'
    else:
        _ip = get_ip_address()
        b = ".".join(_ip.split(".")[:3]) + ".255"

    return b


def create_socket():
    client = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.settimeout(2)
    return client


def decorate_ip(func):
    @wraps(func)
    def wrapper():
        address = func()
        logger.debug("Local IP: " + address)
        return address

    return wrapper


@decorate_ip
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def send_code(cl, broadcast, port):
    cl.sendto(b'1', (broadcast, port))
    return None


def get_response(cl):
    while True:
        try:
            data, addr = client.recvfrom(1024)
            data = json.loads(data.decode('utf-8'))
            _ip, _port = addr
            machine = data.get('machine', None)

            if machine and machine == 'rockpis':
                # print(addr[0])
                client.close()
                #exit(0)
                return _ip 
        except KeyboardInterrupt:
            print("chiudo mestamente")
            client.close()
            exit(1)


if __name__ == "__main__":
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = ''

    broadcast = set_broadcast_address(arg)

    while True:
        try:
            client = create_socket()
            send_code(client, broadcast, PORT)
            address = get_response(client)
            logger.info(f"ROCKPIS IP: {address}")
            break 
        except socket.timeout:
            logger.debug("TIMEOUT: RETRYING")
            continue

    exit()
