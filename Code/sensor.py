import time
import mraa

def NoiseRead():
    noise = mraa.Aio(3)
    NoiseValue = noise.read()
    return NoiseValue

def HumanRead():
    human1 = mraa.Aio(1)
    human2 = mraa.Aio(2)
    return1 = human1.read()
    return2 = human2.read()
    return hretrn1,return2

def ControlRelay(flag):
    relay = mraa.Gpio(62) # GPIO_51
    relay.dir(mraa.DIR_OUT)
    if flag == 1:
        relay.write(1)
    else:
        relay.write(0)
    

if __name__ == "__main__":
    while True:
        print(AirRead())
        print(TemperatureRead())
        ControlRelay(1)
        time.sleep(1)
        ControlRelay(0)
        time.sleep(1)
