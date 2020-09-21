import smbus2
import bme280
import RPi_I2C_driver
from time import *

porta_i2c = 1
endereco = 0x76
bus = smbus2.SMBus(porta_i2c)

calibracao_paramentros = bme280.load_calibration_params(bus, endereco)

dado = bme280.sample(bus, endereco, calibracao_paramentros)

print("ID: " + str(dado.id))
print("Data/Hora: " + str(dado.timestamp))
print("Temperatura: " + str(dado.temperature))
print("Umidade: " + str(dado.humidity))
print("Press  o atmosf  rica: " + str(dado.pressure))

mylcd = RPi_I2C_driver.lcd()


mylcd.lcd_display_string(dado.timestamp, 1)
mylcd.lcd_display_string(dado.temperature, 2)

sleep(2)

mylcd.lcd_clear()

