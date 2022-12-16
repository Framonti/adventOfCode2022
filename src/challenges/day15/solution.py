from src.challenges import read_input_removing_new_line, extract_and_convert_digit_from_string
from scipy.spatial.distance import cityblock

sensors_beacons_data = read_input_removing_new_line('input.txt')
sensors_beacons_split = [sensor_signal.split(':') for sensor_signal in sensors_beacons_data]


def parse_input(sensor_data, beacon_data):
    x_y_sensor_data_split = sensor_data.split(',')
    x_y_sensor_data = extract_and_convert_digit_from_string(
        x_y_sensor_data_split[0]), extract_and_convert_digit_from_string(x_y_sensor_data_split[1])
    x_y_beacon_data_split = beacon_data.split(',')
    x_y_beacon_data = extract_and_convert_digit_from_string(
        x_y_beacon_data_split[0]), extract_and_convert_digit_from_string(x_y_beacon_data_split[1])
    return complex(*x_y_sensor_data), complex(*x_y_beacon_data)


cleaned_sensor_beacon_data = [parse_input(sensor_data=sensor_beacon_data[0], beacon_data=sensor_beacon_data[1]) for
                              sensor_beacon_data in sensors_beacons_split]
sensors_positions = [sensor_beacon_data[0] for sensor_beacon_data in cleaned_sensor_beacon_data]
beacon_positions = [sensor_beacon_data[1] for sensor_beacon_data in cleaned_sensor_beacon_data]


def compute_manhattan_distance(sensor_position, beacon_position):
    return cityblock([sensor_position.real, sensor_position.imag],
                     [beacon_position.real, beacon_position.imag])


manhattan_distances = [compute_manhattan_distance(pair_sensor_beacon_position[0], pair_sensor_beacon_position[1])
                       for pair_sensor_beacon_position in cleaned_sensor_beacon_data]

covered_row_points = set()

ROW = 2_000_000


def save_covered_positions_by_row(sensor_position, manhattan_distance, row_to_check):
    distance_to_row = abs(sensor_position.imag - row_to_check)

    min_covered_x = sensor_position.real - manhattan_distance + distance_to_row
    max_covered_x = sensor_position.real + manhattan_distance - distance_to_row

    for x in range(int(min_covered_x), int(max_covered_x) + 1):
        covered_row_points.add(complex(x, row_to_check))


[(save_covered_positions_by_row(pair[0], pair[1], ROW)) for pair in
 zip(sensors_positions, manhattan_distances)]

# There is a known bacon at row 2_000_000
print(f'first solution: {len(covered_row_points) - 1}')

MIN_X = MIN_Y = 0
MAX_X = MAX_Y = 4_000_000

manhattan_radii = dict()
for sensor_position, manhattan_distance in zip(sensors_positions, manhattan_distances):
    manhattan_radii[sensor_position] = manhattan_distance

descending_diagonal_line_coefficients, ascending_diagonal_line_coefficients = set(), set()
for sensor_position, radius in zip(sensors_positions, manhattan_distances):
    descending_diagonal_line_coefficients.add(sensor_position.imag - sensor_position.real + radius + 1)
    descending_diagonal_line_coefficients.add(sensor_position.imag - sensor_position.real - radius + 1)
    ascending_diagonal_line_coefficients.add(sensor_position.imag + sensor_position.real + radius + 1)
    ascending_diagonal_line_coefficients.add(sensor_position.imag + sensor_position.real - radius + 1)


FREQUENCY_FACTOR = 4_000_000

for a in descending_diagonal_line_coefficients:
    for b in ascending_diagonal_line_coefficients:
        # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        intersection_points = ((b - a) // 2, (a + b) // 2)
        # check belonging to scanned space
        if all(0 < intersection_point < MAX_X for intersection_point in intersection_points):
            # check if intersection point is outside the manhattan radius of sensor positions
            if all(cityblock(intersection_points, [sensor_pos.real, sensor_pos.imag]) > manhattan_radii[sensor_pos] for sensor_pos in sensors_positions):
                tuning_frequency = FREQUENCY_FACTOR * intersection_points[0] + intersection_points[1]
                print(f'second solution: {tuning_frequency}')
                break
