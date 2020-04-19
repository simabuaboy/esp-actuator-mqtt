import time
from machine import Pin, PWM
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'Donkey-Camp 2.4 GHz'
password = 'notinthesamehole'
mqtt_server = '192.168.101.46'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'helloop'
topic_pub = b'hello'
servo = PWM(Pin(4), freq=50, duty=77)
servo.duty(30)
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())