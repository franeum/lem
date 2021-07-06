#!/usr/bin/env python3

## using it to send rockpis ip

import socket
import json


PORT = 37020
message = { "machine": "rockpis" }


def create_socket():
    client = socket.socket(socket.AF_INET, 
                            socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", PORT))
    return client 


def send_response(cl):
    while True:
        try:
            data, addr = cl.recvfrom(1024)
            data = data.decode('utf-8')
            if data and data == '1':
                msg = json.dumps(message)
                cl.sendto(msg.encode(), addr)
                #cl.close()
                #print("chiudo correttamente")
                #exit(0)
        except KeyboardInterrupt:
            cl.close()
            print("key interrupt")
            exit(0)


if __name__ == "__main__":
    client = create_socket()
    send_response(client)
    client.close()
    exit(0)