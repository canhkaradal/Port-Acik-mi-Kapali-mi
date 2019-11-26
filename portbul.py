import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("IP Adresini Giriniz: ")
port = int(input("Port Numarasini Giriniz: "))


def portTara(port):
    if s.connect_ex((host, port)):
        print("Port Kapali")
    else:
        print("Port Acik")

portTara(port)