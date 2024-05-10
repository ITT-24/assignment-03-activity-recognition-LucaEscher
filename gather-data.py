# this program gathers sensor data

import csv
from datetime import datetime
from DIPPID import SensorUDP
import os
import time

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

gathering_is_started = False
running = True
activity = "jumpingjacks"
number = 5

# time that decides how many seconds the data will be gathered
TIME = 10

# id is added in resample.py > therefore it is ignored here
csv_headers = ['timestamp', 'acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z']
start_time = 0
data = []


def save_data():
    with open(f'./data/luca-{activity}-{number}.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # add header row to csv
        writer.writerow(csv_headers)
        writer.writerows(data)


print('Press button 1 to start the data collection!')
while (running):
    if sensor.has_capability('button_1'):
        button_1 = sensor.get_value('button_1')

        if button_1 == 1 and not gathering_is_started:
            print('Starting data collection …')
            gathering_is_started = True
            start_time = time.time()

        if gathering_is_started:
            passed_time = round(time.time() - start_time, 2)
            print(passed_time)

            if sensor.has_capability('accelerometer'):
                acc_x = float(sensor.get_value('accelerometer')['x'])
                acc_y = float(sensor.get_value('accelerometer')['y'])
                acc_z = float(sensor.get_value('accelerometer')['z'])

            if sensor.has_capability('gyroscope'):
                gyro_x = float(sensor.get_value('gyroscope')['x'])
                gyro_y = float(sensor.get_value('gyroscope')['y'])
                gyro_z = float(sensor.get_value('gyroscope')['z'])

            data.append([datetime.now().timestamp(), acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z])

            # gather data for TIME seconds
            if passed_time > TIME:
                save_data()
                print("Data collection finished!")
                running = False
                os._exit(0)

        # if 1 ms is not waited, data is empty when resampling
        time.sleep(0.001)
