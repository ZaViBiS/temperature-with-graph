import gc

import network

# off wifi
network.WLAN(network.STA_IF).active(False)
network.WLAN(network.AP_IF).active(False)

gc.collect()
gc.enable()
