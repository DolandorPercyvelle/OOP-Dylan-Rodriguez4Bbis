class device:
    def __init__(self, mac_address, type, bandwidth, max_bandwidth):
        self.mac_address = mac_address     #
        self.device_type = type     #
        self.bandwidth = 100           #
        self.max_bandwidth = 500           #

    def limit_bandwidth(self, number):     #
        self.bandwidth = number            #

    def free_bandwidth(self):              #
        self.bandwidth = self.max_bandwidth

    def get_info(self):                    #
        return f"MAC Address: {self.mac_address}, Device Type: {self.device_type}, Bandwidth: {self.bandwidth}, Max Bandwidth: {self.max_bandwidth}"


class Router:                               #
    def __init__(self, SSID):
        self.SSID = SSID
        self.devices = []

    def connect_device(self, c_device):
        self.devices.append(c_device)

    def total_bandwidth(self):
        return sum(c_device.bandwidth for c_device in self.devices)

    def get_info(self):
        return f"SSID: {self.SSID}"


router = Router("Dualbit")
# router2= Router("Dualbyte")
device1 = device("00:01:02:03:04:05", "Laptop Victus", 100, 100)
device2 = device("AA:BB:CC:DD:EE:FF", "Pixel 7", 100, 100)
##############################
router.connect_device(device1)
router.connect_device(device2)
device1.limit_bandwidth(20)

print(f"Current bandwidth consumption: {router.total_bandwidth()} Mbps")
