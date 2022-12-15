from src.challenges import read_input_removing_new_line
import re
from scipy.spatial.distance import cityblock

sensors_beacons_data = read_input_removing_new_line('input.txt')
sensors_beacons_split = [sensor_signal.split(':') for sensor_signal in sensors_beacons_data]


def parse_input(sensor_data, beacon_data):
    x_y_sensor_data_split = sensor_data.split(',')
    x_y_sensor_data = int(re.sub('\D', '', x_y_sensor_data_split[0])), int(re.sub('\D', '', x_y_sensor_data_split[1]))
    x_y_beacon_data_split = beacon_data.split(',')
    x_y_beacon_data = int(re.sub('\D', '', x_y_beacon_data_split[0])), int(re.sub('\D', '', x_y_beacon_data_split[1]))
    return complex(*x_y_sensor_data), complex(*x_y_beacon_data)


cleaned_sensor_beacon_data = [parse_input(sensor_data=sensor_beacon_data[0], beacon_data=sensor_beacon_data[1]) for
                              sensor_beacon_data in sensors_beacons_split]


def compute_manhattan_distance(pair_sensor_beacon_position):
    sensor_position = pair_sensor_beacon_position[0]
    beacon_position = pair_sensor_beacon_position[1]
    return cityblock([sensor_position.real, sensor_position.imag],
                     [beacon_position.real, beacon_position.imag])


manhattan_distances = [compute_manhattan_distance(pair_sensor_beacon_position) for pair_sensor_beacon_position in
                       cleaned_sensor_beacon_data]

covered_points = set()

ROW = 2_000_000


def get_covered_positions(sensor_beacon_data, manhattan_distance):
    signal_position = sensor_beacon_data[0]
    distance_to_row = abs(signal_position.imag - ROW)

    min_covered_x = signal_position.real - manhattan_distance + distance_to_row
    max_covered_x = signal_position.real + manhattan_distance - distance_to_row
    for x in range(int(min_covered_x), int(max_covered_x)):
        covered_points.add(complex(ROW, x))


[get_covered_positions(pair[0], pair[1]) for pair in zip(cleaned_sensor_beacon_data, manhattan_distances)]

print(f'first solution: {len(covered_points)}')
