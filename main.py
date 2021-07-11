import stand_up_please



#流光
'''
def water_lights():
    light = []
    #批量设定输出引脚
    out_pin = [13, 14, 15]
    for pin in out_pin:
        light.append(machine.Pin(pin, machine.Pin.OUT))
    while True:
        #light[-1].value(0)
        for point in light:
            point.value(1)
            time.sleep(1)
            point.toggle()
    return 0

def live_led():
    led = PWM(Pin(25))

    led.freq(1000)

    led_duty = 0
    led_direction = 1

    while True:
        led_duty += led_direction
        if led_duty >= 100:
            led_duty = 100
            led_direction = -1
        elif led_duty <= 0:
            led_duty = 0
            led_direction =1
        led.duty_u16(int(led_duty * 655.36))
        if led_duty % 5 ==0:
            print(led_duty)
        time.sleep(0.01)
    return 0
'''
'''
#def bad_apple():
i2c = I2C(id=0, scl=Pin(1), sda=Pin(0), freq = 400_000)
print(i2c.scan())
oled = SSD1306_I2C(128, 64, i2c)
play("ba.bpv", oled)
'''
    
#t1 = Thread(target=live_led, args=())
#t2 = Thread(target=bad_apple, args=())

#t1.start()
#t2.start()

#bad_apple()