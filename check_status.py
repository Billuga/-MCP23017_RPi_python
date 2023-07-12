#!/usr/bin/python

import smbus

bus = smbus.SMBus(1)
addresses = [0x20, 0x21, 0x22, 0x23, 0x24, 0x25]
total_on = []

for address in addresses:
    status = bus.read_byte_data(address, 0x12)  # Checking status of all GPIO pins of port-A
    data = 0x01
    a = hex(address)
    for MyData in range(0, 8):
        state = status & data
        x = MyData + 1
        if state == data:
            #x = MyData + 1
            print("address", a, " GPIO Pin-", x, " of Port-A is High")
            total_on.append("%d")
            data = data << 1
        else:
            data = data << 1
            print("address", a, " GPIO Pin-", x, " of Port-A is Low")

for address in addresses:
    status = bus.read_byte_data(address, 0x13)  # Checking status of all GPIO pins of port-B
    data = 0x01
    a = hex(address)
    for MyData in range(0, 8):
        state = status & data
        x = MyData + 1
        if state == data:
            #print(hex(address))
            print("address", a, " GPIO Pin-", x, " of Port-B is High")
            total_on.append("%d")
            data = data << 1
        else:
            data = data << 1
            print("address", a, " GPIO Pin-", x, " of Port-B is Low")

cont = len(total_on)



