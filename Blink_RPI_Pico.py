# Importando as funções da bibliotecas necessárias
from machine import Pin 
from utime import sleep

# Instaciando um objeto do tipo LED
led = Pin(15, Pin.OUT)

# Laço para piscar o Led 
while True:
  led.value(1)
  sleep(2)
  led.value(0)
  sleep(2)
