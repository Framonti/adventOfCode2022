from src.challenges import read_input_removing_new_line, group_by_separator, sort_and_get_top_n_elem

input_data = read_input_removing_new_line('input.txt')

calorie_split_per_elf_str = group_by_separator(input_data, '')

calorie_split_per_elf = [map(int, calorie_per_elf) for calorie_per_elf in calorie_split_per_elf_str]

tot_cal_per_elf = [sum(calorie_per_elf) for calorie_per_elf in calorie_split_per_elf]

solution1 = max(tot_cal_per_elf)

top_3_elves = sort_and_get_top_n_elem(tot_cal_per_elf, top_n=3)

solution2 = sum(top_3_elves)

print(f'solution1: {solution1}')
print(f'solution2: {solution2}')
