#!/usr/bin/python
import smbus

bus = smbus.SMBus(1)

addresses = [0x20, 0x21, 0x22, 0x23, 0x24, 0x25]
for address in addresses:
    data = 0xFE
    for MyData in range(0, 8):
       # bus.write_byte_data(address, 0x12, data)  # Turning all  OFF, one by one  GPIO A  All pins logic LOW
        bus.write_byte_data(address, 0x13, data)  # Turning all  OFF, one by one  GPIO B  All pins logic LOW
        data = data << 1
       # print(data)
    for MyData in range(0, 8):
        bus.write_byte_data(address, 0x12, data)  # Turning all  OFF, one by one  GPIO A  All pins logic LOW
       # bus.write_byte_data(address, 0x13, data)  # Turning all  OFF, one by one  GPIO B  All pins logic LOW
        data = data << 1
       # print(data)
