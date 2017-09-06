# iptools

Internet Protocol (IP) tools

*Files*

```in_network.py``` - Shows if an IPv4 address matches a base address and wildcard mask

# ```in_network.py```

*Purpose*

Provide a network, wildcard mask and a list of addresses. This script returns
whether the address resides within that network. This works with discontiguous
networks, which sets it apart from many similar tools.

*Usage*

```
Usage: ./in_network.py <network> <mask> <address> [address..N]
```

*Demonstrations*

```
$ ./in_network.py 192.168.80.0 0.0.3.255 192.168.{80,83,86}.2
192.168.80.2    matches net 192.168.80.0    / wildcard mask 0.0.3.255      ? yes
192.168.83.2    matches net 192.168.80.0    / wildcard mask 0.0.3.255      ? yes
192.168.86.2    matches net 192.168.80.0    / wildcard mask 0.0.3.255      ? no
```

But, the beauty comes when you work with discontiguous networks.

```
$ ./in_network.py 192.168.0.0 0.0.248.14 192.168.{79,80}.{1..10}
192.168.79.1    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.79.2    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.79.3    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.79.4    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.79.5    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.79.6    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.79.7    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.79.8    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.79.9    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.79.10   matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.80.1    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.80.2    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? yes
192.168.80.3    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.80.4    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? yes
192.168.80.5    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.80.6    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? yes
192.168.80.7    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.80.8    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? yes
192.168.80.9    matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? no
192.168.80.10   matches net 192.168.0.0     / wildcard mask 0.0.248.14     ? yes
```

*TODO*

* Docker container as a shippable tool
* Package for direct import by others' code
