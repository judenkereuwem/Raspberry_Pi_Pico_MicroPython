from imu import MPU6050
from time import sleep
from machine import Pin, I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

while True:
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)
    tem=round(imu.temperature,2)
    #print("ax",ax,"\t","ay",ay,"\t","az",az,"\t","gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","Temperature",tem,"        ",end="\r")
    print("Accel_X: ", ax)
    print("Accel_Y: ", ay)
    print("Accel_Z: ", az)
    
    print("Gyro_X: ", gx)
    print("Gyro_Y: ", gy)
    print("Gyro_Z: ", gz)
    
    print("Temperature: ", tem)
    print("")
    sleep(0.2)