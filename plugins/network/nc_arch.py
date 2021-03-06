# TODO: Reconfigure for use with netcfg

from genesis.com import *
from genesis.utils import *
from genesis import apis

from api import *
from nctp_ip import *

# rc_net_keys = ('address', 'netmask', 'broadcast', 'gateway')

class ArchNetworkConfig(LinuxIp):
    implements(INetworkConfig)
    platform = ['Arch']
    
    interfaces = None
    
    def __init__(self):
        # self.rcconf = apis.rcconf.RCConf(self.app)
        self.rescan()
    
    def rescan(self):
        self.interfaces = {}
        name = 'eth0'
        # name = 'self.rcconf.get_param('interface')'
        
        if name == '':
            return
        
        iface = NetworkInterface()
        iface.name = name
        iface.type = 'inet'
        iface.auto = True
        self.interfaces[name] = iface
        
        # if self.rcconf.has_param('INTERFACES'):
        #    for key in rc_net_keys:
        #        value = self.rcconf.get_param(key)
        #        if key == 'address':
        #            iface.addressing = 'dhcp' if value == '' else 'static'
        #            iface.params[key] = value
        #
        #            iface.devclass = self.detect_dev_class(iface)
        #            iface.up = shell_status('ifconfig ' + iface.name + '|grep UP') == 0
        #            iface.get_bits(self.app, self.detect_iface_bits(iface))
        #else:
        s = shell('ip -o link list')
        for line in s.split('\n'):
            line = line.strip()
            if line != '':
                name = line.split(':')[1].strip()
                iface = NetworkInterface()
                iface.name = name
                self.interfaces[name] = iface
                iface.devclass = self.detect_dev_class(iface)
                iface.up = (line.find('state UP') != -1)
                iface.get_bits(self.app, self.detect_iface_bits(iface))
                iface.editable = False
   

    def save(self):
        # for iface in self.interfaces.values():
        #    for key in rc_net_keys:
        #        value = iface.params[key]
        #        if iface.addressing == 'dhcp':
        #            value = ''
        #        self.rcconf.set_param(key, value, near='interface')
        return