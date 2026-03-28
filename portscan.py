import socket

target = input("Enter IP Target: ")
port = [21, 22, 23, 80, 443]

for port in ports : 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
