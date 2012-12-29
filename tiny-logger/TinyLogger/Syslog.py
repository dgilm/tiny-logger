#
# Main documentation for twisted UDP development:
# http://twistedmatrix.com/documents/current/core/howto/udp.html
#
# An easy way to test a simple UDPServer:
# nc -u <serverip> 514 <<< "log message"
#

import os
from twisted.internet import protocol, reactor

from FileUtils import FileUtils

class SyslogInput(protocol.DatagramProtocol):

    def __init__(self, logdir):
        self.logdir = logdir
        
    def datagramReceived(self, data, address):
        ipaddr, port = address
        dir = FileUtils.get_dir_to_write(os.path.join(self.logdir, ipaddr))
        print ">>> Writing (%r) into (%s).." % (data, dir)

if __name__ == "__main__":

    import yaml
    config = yaml.load(open('../config'))
    logdir = config['storage']['log_directory']

    reactor.listenUDP(514, SyslogInput(logdir))
    reactor.run()

