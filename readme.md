# 基本说明
用于读取EC11编码器,基于合宙ESP32测试无问题。<br>
clk_pin_gpio为EC11-A线。<br>
data_pin_gpio为EC11-B线。<br>
button_gpio为EC11按钮。<br>
# 用法
~~~
ec11 = Encode(Pin(2, Pin.IN),Pin(3, Pin.IN),Pin(10, Pin.IN)) # 创建ec11对象即可

ec11.num # 获取当前位置
~~~

button_fun内自行按需修改