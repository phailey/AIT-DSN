#!/usr/bin/env python
#
# Usage:
#   python rcf_api_test.py
#
# SSPSim Config:
# 1. Open "MISSION MANAGERS" >  "Test" > "RCFv2 ONLC2"
# 2. Ensure that the Production Id is set to "TestBaseband2"
# 3. Ensure that GVCID is set to (250, 0, *)
# 4. Open "PRODUCTION" > "TestBaseband2"
# 5. Ensure that Spacecraft Id is set to 250
# 6. Ensure that VCID is checked and set to 6
# 7. Ensure the Source field is set to DUMMY. **NOTE**, the
#       generated data will not contain the VCID you set unless
#       you use the DUMMY data source.
# 8. Activate the TM data flow by clicking the green arrow
#       labelled "TM"
# 9. Activate the TM simulation data creation by clicking the
#       green arrow labelled "SIM".
# 10. Activate the Mission Manager interface by clicking the
#       green arrow labelled "SVC"
#
# Run the script per the usage instructions above. You should see
# logging informing you of the various steps and data being sent
# to the telemetry output port. Note, because we're using dummy data
# we will see 0 bytes being output. This is working as expected.
#
# You can confirm that virtual channels are working by using the commented
# out start call in the script instead. Try changing the virtual_channel
# parameter to a number that doesn't match the VCID you set in step 6 above.
# You should see the connection go through but no data will be received.

import datetime as dt
import time

import bliss.sle

rcf_mngr = bliss.sle.RCF(
    hostname='atb-ocio-sspsim.jpl.nasa.gov',
    port=5100,
    inst_id='sagr=LSE-SSC.spack=Test.rsl-fg=1.rcf=onlc2'
)

rcf_mngr.connect()
time.sleep(2)

rcf_mngr.bind()
time.sleep(2)

start = dt.datetime(2017, 01, 01)
end = dt.datetime(2018, 01, 01)
# rcf_mngr.start(start, end, 250, 0, virtual_channel=6)
rcf_mngr.start(start, end, 250, 0, master_channel=True)
time.sleep(20)

rcf_mngr.stop()
time.sleep(2)

rcf_mngr.unbind()
time.sleep(2)

rcf_mngr.disconnect()
time.sleep(2)