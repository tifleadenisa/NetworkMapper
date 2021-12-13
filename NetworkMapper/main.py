import ipaddress
import sys
import nmap
import socket


def testing_ports(addresses, ports):
    ports_names = {80: "HTTP", 443: "HTTPS", 21: "FTP", 22: "FTPS/SSH", 110: "POP3", 995: "POP3 SSL",
                   143: "IMAP", 993: "IMAP SSL", 25: "SMTP", 587: "SMTP SSL", 23: "Telnet", 50: "IPSec",
                   51: "IPSec", 53: "DNS", 3389: "Remote Desktop Protocol", 445: "SMB"}

    found_results = False
    for ipaddr in addresses:
        for port in ports:
            a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            location = (ipaddr, int(port))
            if a_socket.connect_ex(location) == 0:
                found_results = True
                if int(port) in ports_names:
                    print(location[0] + ":" + str(location[1]) + " (" + ports_names.get(int(port)) + ")")
                else:
                    print(location[0] + ":" + str(location[1]))
            a_socket.close()
    if not found_results:
        print("The mentioned ports are not open for the given addresses")


if __name__ == '__main__':

    network = ipaddress.ip_network(sys.argv[1])
    port_parameters = []
    for i in range(2, len(sys.argv)):
        port_parameters.append(sys.argv[i])

    print("The following addresses are up: ")
    up_addresses = []
    for ip_address in network.hosts():
        scanner = nmap.PortScanner()
        host = socket.gethostbyname(str(ip_address))
        scanner.scan(host, '1', '-v')
        if scanner[host].state() == "up":
            up_addresses.append(str(ip_address))
            print(ip_address)

    if len(sys.argv) > 2:
        print("Testing the ports that were given as parameters for the above addresses")
        testing_ports(up_addresses, port_parameters)
    else:
        print("Testing the most used ports(80, 443, 445, 21, 22, 110, 995, 143, 993, 25, 587) for the above addresses")
        testing_ports(up_addresses, [80, 443, 445, 21, 22, 110, 995, 143, 993, 25, 587])
