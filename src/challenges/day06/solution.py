with open('input.txt', 'r') as input_file:
    signal = input_file.read()

PACKET_MARKER_DISTINCT_VALUES = 4


def get_market_length(marker_distinct_values):
    window_buffer = []
    marker_length = 0
    for letter in signal:
        if len(window_buffer) == marker_distinct_values:
            return marker_length
        marker_length += 1
        if letter in window_buffer:
            equal_letter_position = window_buffer.index(letter)
            window_buffer = window_buffer[equal_letter_position + 1:]
        window_buffer.append(letter)


packet_market_length = get_market_length(PACKET_MARKER_DISTINCT_VALUES)
print(f'first solution: {packet_market_length}')

MESSAGE_MARKET_DISTINCT_VALUES = 14
message_market_length = get_market_length(MESSAGE_MARKET_DISTINCT_VALUES)

print(f'second solution {message_market_length}')