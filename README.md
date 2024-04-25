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

![image](https://cdn.hackaday.io/images/7364821436899092461.jpg)

| Name  | Raspberry PI 4 Pin | nRF24LU1+ Pin |
|-------|---------------------|--------------|
| GND   | 6                   | GND          |
| VCC   | 2                   | VDD          |
| PROG  | 18                  | PROG         |
| SCK   | 23                  | SCK          |
| MOSI  | 19                  | MOSI         |
| MISO  | 21                  | MISO         |
| CSN   | 24                  | CSN          |

Better option:

https://vi.aliexpress.com/item/1005001355434931.html?gatewayAdapt=glo2vnm

https://vi.aliexpress.com/item/1005002721886615.html?spm=a2g0o.productlist.main.1.4ad32274sUXdxK&algo_pvid=58e026c8-f268-46bb-9f9c-bc73e7818263&algo_exp_id=58e026c8-f268-46bb-9f9c-bc73e7818263-0&pdp_npi=4%40dis%21VND%21156128%21116969%21%21%216.14%214.60%21%402101e64117140406533791257e8349%2112000021860244334%21sea%21VN%210%21AB&curPageLogUid=WT5CgGtiAwm7&utparam-url=scene%3Asearch%7Cquery_from%3A

## Resources

- [nRF24LU1P_SPI_Flashing](https://github.com/ShigemoriHakura/nRF24LU1P_SPI_Flashing)
- [nrf24lu1p-512-bootloader](https://github.com/ahtn/nrf24lu1p-512-bootloader)
- [MouseJack](https://saturn.ffzg.hr/rot13/index.cgi?action=display_html;page_name=nrf24lu1)
- [Flash Logitech C-U0007](https://hackaday.io/project/6741-crazyradio-for-cheapskates)
- [nrf24lu1 usb dongle](https://www.bartslinger.com/electronics/nrf24lu1-usb-dongle/)
- [Presentation](https://docs.huihoo.com/infoq/qconbeijing/2016/day3/%E6%89%93%E7%A0%B4%E8%A7%84%E5%88%99%EF%BC%8C%E6%88%91%E6%98%AF%E9%BB%91%E5%AE%A2%E4%B8%93%E9%A2%98/8-2-%E7%BB%99%E5%B9%B3%E6%B0%91%E7%9A%84%20Mousejack-%E5%88%98%E5%87%AF%E4%BB%81.pdf)
