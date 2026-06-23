#download: dht library

from machine import Pin
import dht
import time

# Define the GPIO pin connected to the DHT data pin
dht_pin = Pin(21, Pin.IN) 


# Create a DHT object
sensor = dht.DHT11(dht_pin)

time.sleep(1)

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print(f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%")
    except OSError as e:
        print("Failed to read sensor:", e)
    time.sleep(2) # DHT sensors require a minimum delay between readings