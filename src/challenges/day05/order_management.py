class Order:
    def __init__(self, order_raw):
        self.__extract_order_info__(order_raw)

    def __extract_order_info__(self, order_raw):
        order_info_raw_split = order_raw.split(' ')
        order_info_raw = [number for number in order_info_raw_split if number.isnumeric()]
        self.crates_to_move = int(order_info_raw[0])
        self.starting_position = int(order_info_raw[1])
        self.ending_position = int(order_info_raw[2])


def execute_order(crates_positions: dict, order: Order):
    for i in range(order.crates_to_move):
        crate_to_move = crates_positions[order.starting_position].get()
        crates_positions[order.ending_position].put(crate_to_move)
