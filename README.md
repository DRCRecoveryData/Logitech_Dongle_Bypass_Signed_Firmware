# Logitech Dongle Bypass Signed Firmware

![Image](https://github.com/DRCRecoveryData/Logitech_Dongle_Bypass_Signed_Firmware/blob/main/Images/IMG_0263.png)

This repository contains signed firmware for bypassing security measures on Logitech C-U0007 dongles, enabling advanced functionality and customization.

## Flashing Instructions

![Image](https://github.com/DRCRecoveryData/Logitech_Dongle_Bypass_Signed_Firmware/blob/main/Images/IMG_0264.png)

To flash the signed firmware onto your Logitech C-U0007 dongle, follow these steps:

1. Connect your Raspberry PI 4 to the nRF24LU1+ chip as described in the [Pin Connections](#pin-connections) section.
2. Download the latest version of the signed firmware from the [Releases](https://github.com/yourusername/Logitech_Dongle_Bypass_Signed_Firmware/releases) page.
3. Use the provided flashing tool or method to upload the firmware onto the dongle.

## Pin Connections

![image](https://github.com/DRCRecoveryData/Logitech_Dongle_Bypass_Signed_Firmware/assets/85211068/636a0599-d843-442e-b033-8aa856747121)

You can connect the following pins between the Raspberry PI 4 and the nRF24LU1+:

![image](https://github.com/DRCRecoveryData/Logitech_Dongle_Bypass_Signed_Firmware/assets/85211068/01aca9c3-f60b-4077-9124-812b58639f62)

![image](https://github.com/DRCRecoveryData/Logitech_Dongle_Bypass_Signed_Firmware/assets/85211068/7a66f548-f550-4f8c-bf75-4ccbe78a0453)


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
- [MouseJack](https://saturn.ffzg.hr/rot13/index.cgi?action=display_html;page_name=nrf24lu1)
- [Flash Logitech C-U0007](https://hackaday.io/project/6741-crazyradio-for-cheapskates)
