# OTA (Upload Over The Air) for STM32F103
This project is implemented to program BlueBill Board (STM32 Micro-controller)
over the air using a website with ```PHP``` and NodeMCU board to get the code
from the internet and sending it to STM to write it into the Flash Memory
using the Bootloader flashed on the first 9 kB of Flash Memory.


## project video [*(click here)*](https://youtu.be/M2U45CHqeEk)
[![final-project](./OTA-video.png)](https://youtu.be/M2U45CHqeEk)


## Hardware Required
- STM32F103 BlueBill Board
- USB to TTL


## Connection

|    USB to TTL     | STM32F103      |
| -------------     | -------------  |
| TX                | PA10           |
| RX                | PA9            |
| GND               | GND            |



## The project is divided into three mini-projects
### 1. [Website](http://iot-arm.freevar.com/)
The website is responsible for letting the user upload a .hex file to Server to be ready to be received by the GUI.
The website only allows ```.hex``` to be uploaded.

- **TODO:** before compiling the project remember to change the flash size to:
  -  ```FLASH (rx) : ORIGIN = 0x08002400, LENGTH = 55K ``` .



### 2. GUI
takes actions from the user to check for the hex file in the website if there is a hex file 
the user can choose to flash the code to the STM using TTL.


### 3. STM
On reset, STM Bootloader waits for 5 seconds if there is any code received from TTL.
 If any, it will first erase the application area and then flash the code received.
Once it finished, it will run the application code after 5 seconds.
If no code received from TTL for 5 seconds, it will jump to latest flashed application code.
- **NOTE:**  
  - you need to edit SSID & PASSWORD  (and if needed IPserver & Website) in ```main.h``` file.
  - I used local PHP Server because the free online server take much time to flash the code.
  - size of Bootloader changed in ```FPEC_config.h``` file.
