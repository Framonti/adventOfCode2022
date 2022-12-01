import itertools

with open('input.txt', 'r') as input_file:
    input_data = input_file.readlines()

input_data_without_new_line = [calorie_value[:-1] for calorie_value in input_data]

calorie_split_per_elf_str = [list(group) for is_key, group in itertools.groupby(input_data_without_new_line,
                                                                                lambda sep: sep == '') if not is_key]

calorie_split_per_elf = [map(int, calorie_per_elf) for calorie_per_elf in calorie_split_per_elf_str]

tot_cal_per_elf = [sum(calorie_per_elf) for calorie_per_elf in calorie_split_per_elf]

solution1 = max(tot_cal_per_elf)

sorted_tot_cal_per_elf = sorted(tot_cal_per_elf, reverse=True)
top_3_elves = sorted_tot_cal_per_elf[:3]

solution2 = sum(top_3_elves)

print(f'solution1: {solution1}')
print(f'solution2: {solution2}')
