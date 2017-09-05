#!/usr/bin/env python

"""
Wildcard mask match
Answers the question, "Will this address match this net/mask pair?"
"""

try:
    from socket import inet_aton as socket_aton
    from socket import error as socket_error
    from sys import argv as sysargv
except ImportError as e:
    raise SystemExit("Import error: {}".format(e))
except Exception as e:
    raise SystemExit("ERROR: {}".format(e))

class Address(object):
""" IPv4 address object """

    def __init__(self, address='0.0.0.0'):
        """ IPv4 address information """
        self.address = address
        self.isvalid = valid_ipv4(self.address)
        self.value = addr_to_dec(self.address)
        self.bits = addr_bits(self.address)

def addr_to_dec(address):
    """ Convert IPv4 address string to an integer value """
    s = address.split('.')
    if len(s) == 4:
        return ((int(s[0]) << 24)
                + (int(s[1]) << 16)
                + (int(s[2]) << 8)
                + int(s[3]))

def octet_bits(octet):
    """ Return string of eight bits from an IPv4 octet """
    s = ''
    octet = int(octet)
    while octet:
        s = "1" + s if octet & 1 == 1 else "0" + s
        octet /= 2
    return s.zfill(8)

def addr_bits(address):
    """ Return an IPv4 address string as bits separated by periods """
    octet_list = address.split('.')
    return (
        octet_bits(int(octet_list[0]))
        + '.' + octet_bits(int(octet_list[1]))
        + '.' + octet_bits(int(octet_list[2]))
        + '.' + octet_bits(int(octet_list[3]))
    )

def display_usage(progname):
    """ How does one use this script ? """
    print("Usage: {} <network> <mask> <address> [address..N]".format(progname))
    raise SystemExit

def valid_ipv4(address):
    """ Valid IPv4 address: True or False """
    try:
        socket_aton(address)
    except socket_error:
        return False
    return True

def display_all(net, mask, ip):
    """ Produce report """
    msg = "yes" if net.value | mask.value == ip.value | mask.value else "no"
    print(
        "{:15} matches net {:15} / wildcard mask {:15}? {}".format(
            ip.address,
            net.address,
            mask.address,
            msg
        )
    )

def main(addresses):
    """ Main execution """
    network = Address(addresses[0])
    wildcard_mask = Address(addresses[1])
    if not valid_ipv4(network.address) or not valid_ipv4(wildcard_mask.address):
        raise SystemExit('ERROR: Invalid network or mask {}/{}'.
            format(network.address, wildcard_mask.address))
    for address in addresses[2:]:
        if not valid_ipv4(address): continue
        ip = Address(address)
        display_all(network, wildcard_mask, ip)

if __name__ == '__main__':
    if len(sysargv) < 3: display_usage(sysargv[0])
    main(sysargv[1:])
