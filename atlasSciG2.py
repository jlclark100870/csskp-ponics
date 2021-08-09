import time # Time access and conversions
from binascii import hexlify
from array import array
import smbus

class i2c():
    def __init__(self, addr, port, hardwareLock):
        try:
            self.addr = addr
            self.bus = smbus.SMBus(port)
            self.hardwareLock = hardwareLock
        except:
            raise

    def write_i2c_block_data(self, byte, data):
        try:
            if self.hardwareLock:
                with self.hardwareLock:
                    self.bus.write_i2c_block_data(self.addr, byte, data)
            else:
                self.bus.write_i2c_block_data(self.addr, byte, data)
        except Exception as e:
            print(e)

    def read_nbytes_data(self, data, n): # For sequential reads > 1 byte
        if self.hardwareLock:
            with self.hardwareLock:
                return self.bus.read_i2c_block_data(self.addr, data, n)
        else:
            return self.bus.read_i2c_block_data(self.addr, data, n)

    def f_to_4bytes(self, x):
        x = int(x)
        return [x>>24, x>>16 & 0xFF, x>>8 & 0xFF, x & 0xFF]

class ph_oem(i2c):
    def __init__(self, addr, port, hardwareLock = False):
        try:
            i2c.__init__(self, addr, port, hardwareLock)
            self.write_i2c_block_data(0x06,[0x04]) # activate device
        except:
            raise
    def read(self):
        bytes_array = self.read_nbytes_data(0x16, 4)
        ph_hex = ''.join('{:02x}'.format(x) for x in bytes_array)
        return float.fromhex(ph_hex)/1000

    def write_temp(self, temp):
        if temp:
            data = self.f_to_4bytes(temp*100)
            self.write_i2c_block_data(0x0E,data) # send temp as 4 bytes

    def read_temp(self):
        bytes_array = self.read_nbytes_data(0x12, 4)
        ph_temp_hex = ''.join('{:02x}'.format(x) for x in bytes_array)
        return float.fromhex(ph_temp_hex)/100

    def calibration_state(self):
        return str(self.read_nbytes_data(0x0D, 1)[0]) # return str

    def calibration_clear(self):
        self.write_i2c_block_data(0x0C,[1]) # midpoint calibration set cmd

    def calibration_low(self, value):
        data = self.f_to_4bytes(value*1000)
        self.write_i2c_block_data(0x08, data) # send cal as 4 bytes
        time.sleep(0.1) # wait for the calibration event to finish
        self.write_i2c_block_data(0x0C,[2]) # midpoint calibration set cmd

    def calibration_mid(self, value):
        data = self.f_to_4bytes(value*1000)
        self.write_i2c_block_data(0x08, data) # send cal as 4 bytes
        time.sleep(0.1) # wait for the calibration event to finish
        self.write_i2c_block_data(0x0C,[3]) # midpoint calibration set cmd

class ec_oem(i2c):
    def __init__(self, addr, port, hardwareLock = False):
        try:
            i2c.__init__(self, addr, port, hardwareLock)
            self.write_i2c_block_data(0x06,[0x01]) # activate device
        except:
            raise

    def read(self):
        bytes_array = self.read_nbytes_data(0x18, 4)
        ec_hex = ''.join('{:02x}'.format(x) for x in bytes_array)
        return float.fromhex(ec_hex)/100000

    def read_temp(self):
        bytes_array = self.read_nbytes_data(0x14, 4)
        ph_temp_hex = ''.join('{:02x}'.format(x) for x in bytes_array)
        return float.fromhex(ph_temp_hex)/100
    def write_temp(self, temp):
        if temp:
            data = self.f_to_4bytes(temp*100)
            self.write_i2c_block_data(0x10, data) # send temp as 4 bytes

    def calibration_state(self):
        return str(self.read_nbytes_data(0x0F, 1)[0]) # return str

    def calibration_clear(self):
        self.write_i2c_block_data(0x0E,[0x01]) # midpoint calibration set cmd

    def calibration_dry(self):
        self.write_i2c_block_data(0x0E,[0x02]) # midpoint calibration set cmd

    def calibration_single(self, value):
        data = self.f_to_4bytes(value*100) # uS * 100
        self.write_i2c_block_data(0x0A,data) # send cal as 4 bytes
        time.sleep(0.1) # wait for the calibration event to finish
        self.write_i2c_block_data(0x0E,[0x03]) # midpoint calibration set cmd

if __name__ == "__main__":
    from threading import Lock
    i2cLock = Lock()
    ph = ph_oem(0x63, 1, i2cLock)
    print(ph.read())
    ec = ec_oem(0x64, 1, i2cLock)
    print(ec.read())


