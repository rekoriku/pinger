from ping3 import ping as pingi3
from collections import deque
from functools import reduce
import time
import json
from colorama import init, Fore, Back, Style
init(autoreset=True)


def average(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)


def dicJson(vals):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    dic = {'data': vals, 'aika': current_time}
    data = [dic]
    return data


def saveJson(data):
    with open('log.json') as data_file:
        old_data = json.load(data_file)
        data = old_data + data
        with open('log.json', 'w') as json_file:
            json.dump(data, json_file, indent=1)


def saveLog(textresult):
    log = open("log.txt", "a")
    log.write(str(textresult) + "\n")
    log.close()
    return 0


class Pinger:
    def __init__(self, hostname, quelen, delay):
        self.hostname = hostname #host name that will be pinged
        self.quelen = quelen #deques max length
        self.delay = delay
        self.pings = deque([], self.quelen)
    #hostname = "google.com"
    #pings = deque([], maxlen=60)

    def roundstr(self,val):
        return str(round(val))

    def start(self):
        while True:
            rnd = self.roundstr
            pings = self.pings

            pings.appendleft(pingi3(self.hostname, unit='ms')) # push ping value to deques first index
            currentping = rnd(pings[0]) #round first index val and convert to string
            averageping = rnd(average(pings)) #convert average ping vals to string
            maxping = rnd(max(pings)) #convert max ping to string
      
            print(Fore.LIGHTBLUE_EX + 'current ping: ' + currentping)
            print(Style.DIM + Fore.MAGENTA + 'average ping: ' + averageping)
            print(Style.DIM + Fore.RED + 'max ping: ' + maxping)
            print('')
            # print('------------------------')
            # saveJson(dicJson(pings[0]))

            #### Delay for 1 seconds ####
            time.sleep(self.delay)

raw = input('Enter ping address: ')
ping = Pinger(raw, 60, 1)
ping.start()
