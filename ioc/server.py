from softioc import builder
import time


class ATIPServer(object):
    def __init__(self, pvs):
        self._create_records(pvs)

    def _create_records(self, pvs):
        start = time.time()
        for pv in pvs:
            builder.SetDeviceName(pv)
            builder.aIn('I', initial_value=0.1)
            builder.aOut('SETI', initial_value=0.1)
        print("    Time per pv: {0}".format((time.time() - start)/len(pvs)))
