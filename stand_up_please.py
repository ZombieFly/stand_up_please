from machine import Pin, I2C
from time import sleep

from esp8266_i2c_lcd import I2cLcd

def button_status(button, expected_value):
    while True:
        if button.value() == expected_value:
            sleep(0.01)
            if button.value() == expected_value:
                return 0

class Timer:
    def __init__(self):
        self.time_point = [0, 0]
    def output(self, put_time):
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr(str(self.time_point[0])+' m')
            lcd.move_to(0,1)
            lcd.putstr(str(self.time_point[1])+' s')
    def oh_time_is_up(self, lcd, expected_value):
        self.output(self.time_point)
        while True:
            sleep(1)
            self.time_point[1] += 1
            if self.time_point[1] == 60:
                self.time_point[1] = 0
                self.time_point[0] += 1
            self.output(self.time_point)
            if self.time_point == expected_value:
                return 1
                
    def clear(self):
        self.time_point = [0, 0]
        
'''
初始化1602
'''
DEFAULT_I2C_ADDR = 0x27
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
print(i2c.scan())
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
lcd.putstr('Do not sit for  long time!')
sleep(3)

'''
初始化按钮
'''
button = Pin(21, Pin.IN, Pin.PULL_UP)

'''
初始化计时器数据
'''
time_point = [0, 0]

timer = Timer()
while True:
    timer.oh_time_is_up(lcd, [45,0])
    while button.value():
        print(button.value())
        lcd.backlight_off()
        sleep(0.5)
        lcd.backlight_on()
        sleep(0.5)
    timer.clear()
    sleep(5)
    button_status(button, 0)
    
        