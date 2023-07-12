#!/usr/bin/python
import smbus
bus = smbus.SMBus(1)  # For revision 1 Raspberry Pi, change to bus = smbus.SMBus(1) for revision 2.
addresses = [0x20, 0x21, 0x22, 0x23, 0x24, 0x25]

for address in addresses:
    bus.write_byte_data(address, 0x00, 0x00)  # Set all of bank A to outputs
    bus.write_byte_data(address, 0x01, 0x00)  # Set all of bank B to outputs

print("Set all of bank to outputs")
