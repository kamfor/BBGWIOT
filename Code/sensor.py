import time
import mraa

def NoiseRead():
    noise = mraa.Aio(7) #AIN6
    NoiseValue = noise.read()
    return 1023-NoiseValue

def ProxRead():
    prox = mraa.Aio(3) #AIN2
    return1 = prox.read()
    return 1023-return1

def ControlRelay1(flag):
    relay = mraa.Gpio(62) # GPIO_51
    relay.dir(mraa.DIR_OUT)
    if flag == 1:
        relay.write(1)
    else:
        relay.write(0)

def ControlRelay2(flag):
    relay = mraa.Gpio(60) # GPIO_50
    relay.dir(mraa.DIR_OUT)
    if flag == 1:
        relay.write(1)
    else:
        relay.write(0)
    

if __name__ == "__main__":
    while True:
        print(NoiseRead)
        print(ProxRead)
        ControlRelay1(1)
        time.sleep(1)
        ControlRelay1(0)
        time.sleep(1)
	ControlRelay2(1)
	time.sleep(1)
	ControlRelay2(0)
	time.sleep(1)
