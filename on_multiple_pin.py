#!/usr/bin/python
import smbus
import sys
#from init import *
#address, bank, pin1 , pin2 , pin3 , pin4  , pin5 , pin6 , pin7 , pin8

pin1 = 0
pin2 = 0
pin3 = 0
pin4 = 1
pin5 = 0
pin6 = 0
pin7 = 0
pin8 = 0

if pin1 == 1:
    pin1 = 0b00000001
if pin2 == 1:
    pin2 = 0b00000010
if pin3 == 1:
    pin3 = 0b00000100
if pin4 == 1:
    pin4 = 0b00001000
if pin5 == 1:
    pin5 = 0b00010000
if pin6 == 1:
    pin6 = 0b00100000
if pin7 == 1:
    pin7 = 0b01000000
if pin8 == 1:
    pin8 = 0b10000000

address = 0x20  # I2C address of MCP23017
bank = "a"

# Set the correct register for the banks
if bank == "a":
    register = 0x12
elif bank == "b":
    register = 0x13
else:
    print("Error! Bank must be a or b")
    sys.exit()

bus = smbus.SMBus(1)  # For revision 1 Raspberry Pi, change to bus = smbus.SMBus(1) for revision 2.

data = [0x09,0x00, pin1 + pin2 + pin3 + pin4  + pin5 + pin6 + pin7 + pin8]
bus.write_i2c_block_data(address, register, data)
