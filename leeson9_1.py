import time


class TrafficLight:
    __color = None

    def running(self):
        __color = 'red'
        print(__color)
        time.sleep(1)
        sec = 1
        while sec <=6:
            print(sec)
            time.sleep(1)
            sec += 1
        __color = 'yellow'
        print(__color)
        time.sleep(1)
        sec = 1
        while sec <= 1:
            print(sec)
            time.sleep(1)
            sec += 1
        __color = 'green'
        print(__color)

test = TrafficLight()
test.running()



