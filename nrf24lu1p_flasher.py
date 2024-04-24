#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import os

# Script setup. Use this as a documentation to cable the Crazyradio or modify
# if you want to cable it differently.
# Name   Pin on raspi     Pin on NRF24LU1P
#-------------------------------------------
GND   =   6              # 9
RESET =   18             # 3
PROG  =   22             # 2
SCK   =   23             # 4
MOSI  =   19             # 6
MISO  =   21             # 8
CS    =   24             # 10

CS_ENABLE = GPIO.LOW
CS_DISABLE = GPIO.HIGH

# SPI commands
WREN = 0x06
WRDIS = 0x04
RDSR = 0x05
WRSR = 0x01
ERASE_PAGE = 0x52
ERASE_ALL = 0x62
PROGRAM = 0x02
READ = 0x03
RDFPCR = 0x89
RDISMB = 0x85
ENDEBUG = 0x86
RDYN = 0x10

FSR_RDYN = 0x10
FSR_WEN = 0x20
FSR_INFEN = 0x08

CHIP_ID = [0] * 5

def init_gpios():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(RESET, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(PROG, GPIO.OUT, initial=GPIO.HIGH)

def check_connection():
    return GPIO.input(RESET) != 0

def reset_in_prog():
    GPIO.output(RESET,

