from collections import namedtuple

Network = namedtuple('Network', [
    'network_name',
    'network_shortname',
    'subnet_name',
    'pubkeyhash',
    'wif_prefix',
    'scripthash',
    'magicbytes'
])

networks = (
    # Peercoin mainnet
    Network("Peercoin", "ppc", "mainnet", b'37', b'b7', b'75', b'e6e8e9e5'),
    # Peercoin testnet
    Network("Peercoin", "tppc", "testnet", b'6f', b'ef', b'c4', b'cbf2c0ef')
)

def query(query):
    '''find matching parameter among the networks'''

    for network in networks:
        for field in network:
            if field == query:
                return network
