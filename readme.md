# 一个于Pico开发的久坐提醒工具

| 所需硬件   | 备注 |
| ---------- | ---- |
| lcd1602    |      |
| pico开发板 |      |
| PCF8574    |      |

## 硬件引脚对应表

（可依实际情况同时更改程序和硬件接线方案）

| PCF8574 | pico(GP) |
| ------- | -------- |
| GND     | GND      |
| VCC     | VBUS     |
| SDA     | GP8      |
| SCL     | GP9      |

## 程序设定

更改 `stand_up_please.py` 中的 `[45, 0]` 即可更改倒计时时间

```python
timer.oh_time_is_up(lcd, [45,0])
```

