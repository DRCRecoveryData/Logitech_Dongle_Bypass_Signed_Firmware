# Logitech Dongle Bypass Signed Firmware

This repository contains signed firmware for bypassing security measures on Logitech C-U0007 dongles, enabling advanced functionality and customization.

## Flashing Instructions

To flash the signed firmware onto your Logitech C-U0007 dongle, follow these steps:

1. Connect your Raspberry PI 4 to the nRF24LU1+ chip as described in the [Pin Connections](#pin-connections) section.
2. Download the latest version of the signed firmware from the [Releases](https://github.com/yourusername/Logitech_Dongle_Bypass_Signed_Firmware/releases) page.
3. Use the provided flashing tool or method to upload the firmware onto the dongle.

## Pin Connections

You can connect the following pins between the Raspberry PI 4 and the nRF24LU1+:

| Name  | Raspberry PI 4 Pin | nRF24LU1+ Pin |
|-------|---------------------|--------------|
| GND   | 6                   | GND          |
| VCC   | 2                   | VDD          |
| PROG  | 18                  | PROG         |
| SCK   | 23                  | SCK          |
| MOSI  | 19                  | MOSI         |
| MISO  | 21                  | MISO         |
| CSN   | 24                  | CSN          |

## Resources

- [nRF24LU1P_SPI_Flashing](https://github.com/ShigemoriHakura/nRF24LU1P_SPI_Flashing)
- [nrf24lu1p-512-bootloader](https://github.com/ahtn/nrf24lu1p-512-bootloader)
