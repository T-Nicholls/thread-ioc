from pkg_resources import require
require('cothread==2.12')
require('epicsdbbuilder==1.0')

import server
from softioc import builder, softioc
from threading import Thread, Event
import time

# Create thread
class thread_test(object):
    def __init__(self):
        self.flag = Event()
        self.thread = Thread(target=self.target_function)
        self.thread.setDaemon(True)
        self.thread.start()

    def target_function(self):
        while True:
            if self.flag.is_set() is True:
                pass

# Create PVs.
pvs1 = ['PV-{0}-PC-01'.format(i + 1) for i in range(4000)]
pvs1 = ['PV-{0}-PC-02'.format(i + 1) for i in range(4000)]

# Create 4000 aIn and 4000 aOut records without background thread running.
print("Without thread:")
start = time.time()
svr = server.ATIPServer(pvs)
print('    Total time: {0}'.format(time.time() - start))

# Start background thread
th = thread_test()

# Create 4000 aIn and 4000 aOut records with background thread running.
print("With thread:")
start = time.time()
svr = server.ATIPServer(pvs)
print('    Total time: {0}'.format(time.time() - start))

# Start the IOC.
builder.LoadDatabase()
softioc.iocInit()

softioc.interactive_ioc(globals())
