from src.challenges import read_input_removing_new_line, group_by_separator

input_data = read_input_removing_new_line('input.txt')

calorie_split_per_elf_str = group_by_separator(input_data, '')

calorie_split_per_elf = [map(int, calorie_per_elf) for calorie_per_elf in calorie_split_per_elf_str]

tot_cal_per_elf = [sum(calorie_per_elf) for calorie_per_elf in calorie_split_per_elf]

solution1 = max(tot_cal_per_elf)

sorted_tot_cal_per_elf = sorted(tot_cal_per_elf, reverse=True)
top_3_elves = sorted_tot_cal_per_elf[:3]

solution2 = sum(top_3_elves)

print(f'solution1: {solution1}')
print(f'solution2: {solution2}')
