from src.challenges import read_input_removing_new_line

input_ids_to_clean = read_input_removing_new_line('input.txt')

ids_to_clean_per_elves_pair = [ids.split(',') for ids in input_ids_to_clean]

delimiter_id_to_clean_per_elf_pair = [[list(map(int, elves_pair_ids[0].split('-'))),
                                       list(map(int, elves_pair_ids[1].split('-')))]
                                      for elves_pair_ids in ids_to_clean_per_elves_pair]


def is_complete_overlap(first_elf_ids, second_elf_ids):
    return (first_elf_ids[1] <= second_elf_ids[1] and first_elf_ids[0] >= second_elf_ids[0]) or \
           (second_elf_ids[1] <= first_elf_ids[1] and second_elf_ids[0] >= first_elf_ids[0])


is_complete_overlap_mask = [is_complete_overlap(elves_pair_ids[0], elves_pair_ids[1])
                            for elves_pair_ids in delimiter_id_to_clean_per_elf_pair]

first_solution = sum(is_complete_overlap_mask)
print(f'first solution: {first_solution}')


def is_partial_overlap(first_elf_ids, second_elf_ids):
    return (first_elf_ids[0] <= second_elf_ids[1]) and \
           (second_elf_ids[0] <= first_elf_ids[1])


is_partial_overlap_mask = [is_partial_overlap(elves_pair_ids[0], elves_pair_ids[1])
                           for elves_pair_ids in delimiter_id_to_clean_per_elf_pair]

second_solution = sum(is_partial_overlap_mask)
print(f'second solution: {second_solution}')
