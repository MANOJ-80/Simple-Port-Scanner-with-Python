#!/usr/bin/python3

import socket

def portScanner(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        
        result = s.connect_ex((host, port))
        if result != 0:
            print(f"The port {port} is closed")
        else:
            print(f"The port {port} is open")
            
        s.close()  
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    host = input("Enter the IP you want to scan: ")
    port = int(input("Enter the port you want to scan: "))
    
    portScanner(host, port)
