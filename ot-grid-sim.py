from time import sleep
import random

ticks = 0

feeder_data = {'voltage': 200, 'current': 500, 'capacity': 1000, 'breaker': "normal"}

def get_feeder_data(ticks):
    while ticks < 20:
        if feeder_data['breaker'] == "tripped":
            break
        ticks += 1
        feeder_data['voltage'] = random.randint(190, 210)
        feeder_data['current'] = random.randint(400, 1200)
        sleep(1)
        check_feeder_data()
        print(feeder_data['voltage'], feeder_data['current'], feeder_data['capacity'], feeder_data['breaker'])

def check_feeder_data():
    if feeder_data['current'] > feeder_data['capacity']:
        print("Warning: Current exceeds capacity!")
        feeder_data['breaker'] = "tripped"

get_feeder_data(ticks)