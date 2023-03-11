from machine import Pin

class Encode(object):
    def __init__(self,clk_pin_gpio,data_pin_gpio,button_gpio):
        self.clk_pin = clk_pin_gpio
        self.clk_pin.irq(handler=self.encode_value,trigger=Pin.IRQ_FALLING)
        self.data_pin = data_pin_gpio
        self.button = button_gpio
        self.button.irq(handler=self.button_fun,trigger=Pin.IRQ_FALLING)
        self.num = 0

    def encode_value(self,gpio):
        if self.clk_pin.value() != self.data_pin.value():
            self.num -= 1
        else:
            self.num += 1
    
    def button_fun(self,gpio):
        print('hello')
