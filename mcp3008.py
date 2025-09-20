import spidev

class MCP3008:
    def __init__(self, bus=0, device=0, max_speed_hz=1350000, vref=3.3):
        self.vref = vref
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = max_speed_hz
        self.spi.mode = 0  

    def read(self, channel):
        if not 0 <= channel <= 7:
            raise ValueError("Channel must be 0-7")

        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        value = ((adc[1] & 3) << 8) | adc[2]
        return value

    def read_voltage(self, channel):
        value = self.read(channel)
        return (value * self.vref) / 1023

    def close(self):
        self.spi.close()
