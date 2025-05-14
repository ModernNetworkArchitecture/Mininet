#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.link import TCLink
from mininet.log import setLogLevel

class FashionUMKMTopo(Topo):
    def build(self):
        # Switch pusat komunitas fashion
        s1 = self.addSwitch('s1')

        # Cloud server node (tempat VNF dan marketplace)
        cloud = self.addHost('cloud', ip='10.0.0.100/24')
        self.addLink(cloud, s1, bw=100)

        # UMKM nodes
        umkm_list = {
            'batikjogja': '10.0.0.1',
            'modestbandung': '10.0.0.2',
            'ecobali': '10.0.0.3',
            'resellerjakarta': '10.0.0.4'
        }

        for name, ip in umkm_list.items():
            host = self.addHost(name, ip=f'{ip}/24')
            self.addLink(host, s1, bw=10)

def run():
    topo = FashionUMKMTopo()
    net = Mininet(topo=topo,
                  controller=RemoteController,
                  link=TCLink,
                  switch=OVSSwitch,
                  autoSetMacs=True)
    
    # Connect ke Ryu SDN controller (localhost:6633)
    net.addController('ryu', controller=RemoteController, ip='127.0.0.1', port=6633)
    
    net.start()
    print("Jaringan UMKM Fashion sudah aktif. Coba ping antar UMKM atau ke cloud.")
    net.pingAll()
    net.interact()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
