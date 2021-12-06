import ipaddress
import sys
import nmap
import socket
import time

if __name__ == '__main__':

    print(sys.argv)
    network = ipaddress.ip_network(sys.argv[1])
    print(network)
    print(network.num_addresses)

    print("Now we check if an addres is up or not")

    up_addr = []

    t1 = time.time()
    for ip_addr in network.hosts():
        scanner = nmap.PortScanner()
        host = socket.gethostbyname(str(ip_addr))
        scanner.scan(host, '1', '-v')
        print("IP Status for ", ip_addr, " is ", scanner[host].state())
        if scanner[host].state() == "up":
            up_addr.append(str(ip_addr))

    print("--------------")
    t2 = time.time()
    print("i have tested connections for " + str((t2-t1) / 60.0) + " minutes")
    print("--------------")
    print("the following addresses are up: ")
    for x in up_addr:
        print(x)

    up_addr1 = ["192.168.2.1", "192.168.2.110", "192.168.2.197"]

    print("Testing the most used ports(80, 443, 445, 21, 22, 110, 995, 143, 993, 25, 587) for the above addresses")

    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for x in up_addr:

        location = (x, 80)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + ":" + str(location[1]) + " (HTTP)")
        location = (x, 443)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + ":" + str(location[1]) + " (HTTPS)")
        location = (x, 445)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + ":" + str(location[1]))
        location = (x, 21)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + ":" + str(location[1]) + " (FTP)")
        location = (x, 22)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + ":" + str(location[1]) + " (FTPS/SSH)")
        location = (x, 110)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + ":" + str(location[1]) + " (POP3)")
        location = (x, 995)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + ":" + str(location[1]) + " (POP3 SSL)")
        location = (x, 143)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + ":" + str(location[1]) + " (IMAP)")
        location = (x, 993)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + ":" + str(location[1]) + " (IMAP SSL)")
        location = (x, 25)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + ":" + str(location[1]) + " (SMTP)")
        location = (x, 587)
        if a_socket.connect_ex(location) == 0:
            print(location[0] + " " + str(location[1]) + " (SMTP SSL)")

        # print(x)
        # if a_socket.connect_ex(location) == 0:
        #     print("port is open")
        # else:
        #     print("port is not open")


