from machine import Pin
from utime import sleep

botao = Pin(0, Pin.IN, Pin.PULL_UP)  # Botão conectado ao pino 0

while True:
    botao_estado = botao.value()  # Lê o estado do botão
    if botao_estado == 0:  # Botão pressionado
        print("Botão pressionado!")
    else:
        print("Botão liberado!")
    sleep(0.5)
