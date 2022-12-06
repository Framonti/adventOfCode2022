with open('input.txt', 'r') as input_file:
    signal = input_file.read()

window_buffer = []
marker_length = 0
for letter in signal:
    if len(window_buffer) == 4:
        break
    marker_length += 1
    if letter in window_buffer:
        equal_letter_position = window_buffer.index(letter)
        window_buffer = window_buffer[equal_letter_position + 1:]
        window_buffer.append(letter)
    else:
        window_buffer.append(letter)

print(f'first solution: {marker_length}')
