import ipaddress
import sys


if __name__ == '__main__':
    print("hello")
    print(sys.argv)
    network = ipaddress.ip_network(sys.argv[1])
    print(network)
    print(network.num_addresses)

    # Iterating through the usable addresses on the network:
    for x in network.hosts():
        print(x)