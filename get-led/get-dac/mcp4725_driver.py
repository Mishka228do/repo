import smbus
diapa = 5.0
class MCP4725:
    def __init__(self, range, address=0x61, verbose = False):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.diap= range
        self.verbose = verbose


    def dinit(self):
        self.bus.close()
        
    def set_number(self, number):
        if not isinstance(number, int):
            print("OSHIBKA3")
        if not (0 <= number <= 4095):
            print("OSHIBKARAZRIADNOSTY")
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)
        if self.verbose:
            print(f"CHISLO - {number}, OTPR I2C DATA - [0x{(self.address << 1) :02x}, 0x{first_byte:02x}, 0x{second_byte:02X}]\n")
    def set_voltage(self, voltage):
        if 0 <= voltage <= self.diap:
            self.set_number(int(voltage/self.diap * 4095))
        else:
            print("OSHIBKA2")



if __name__ == "__main__":
    try:
        dac = MCP4725(diapa, True)

        while True:
            try:
                voltage = float(input())
                dac.set_voltage(voltage)

            except ValueError:
                print("OSHIBKA1")
    finally:
        dac.dinit()
        
