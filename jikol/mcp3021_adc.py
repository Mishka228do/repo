import smbus

class MCP4725:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)

        self.address = 0x4D

        self.dinamic_range= dynamic_range
        self.verbose = verbose

    def dinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(data, upper_data_byte, lower_data_byte, number)
        return number
    def v(self):
        return self.get_number() / 255 * self.dynamic_range

if __name__ == "__main__":
    try:
        dac = MCP4725(5.2) 
        while True:
            print(dac.v()) 
            time.sleep(1)
    finally:
        dac.dinit()