from time import sleep

class TrafficLight:

    colors = ('red', 'yellow', 'green')
    delay = (1, 1, 1)

    def __init__(self):
        self.__color = None

    def running(self):
        while True:
            for i in self.colors:
                self.__color = i
                print(self.__color)
                sleep(self.delay[self.colors.index(self.__color)])

traffic_light = TrafficLight()
traffic_light.running()