| pin | status |       |
| --- | ------ | ----- |
| 3   | **ok** | reset |
| 5   | no     |       |
| 7   | no     |       |
| 8   | **ok** | d/c   |
| 10  | **ok** |       |
| 11  | **ok** |       |
| 12  | no     |       |
| 13  | **ok** |       |
| 15  | **ok** |       |
| 16  | no     |       |
| 18  | **ok** |       |
| 19  | **ok** |       |
| 21  | **ok** |       |
| 22  | **ok** |       |
| 23  | **ok** |       |
| 24  | **ok** |       |

cs_pin = digitalio.DigitalInOut(board.pin.SPI2_CS)  
dc_pin = digitalio.DigitalInOut(board.pin.GPIO0_B7)  
reset_pin = board.pin.GPIO0_C0
