FILE = "example.txt"
STARTING_POSITION = 50

def read_file(file_input):
    with open(file_input, 'r') as file:
        lines = file.readlines()
    for x, line in enumerate(lines):
        lines[x] = line.strip('\n')
    return lines

def lines_preprocessing(lines):
    processed_lines = []
    for line in lines:
        processed_lines.append([line[0],int(line[1:])])
    return processed_lines

def count_zeros(list_of_instructions):
    count = 0
    position = STARTING_POSITION
    for direction, steps in list_of_instructions:
        if direction == 'R':
            position = (position + steps) % 100
        else:
            position = (position - steps) % 100
        if position == 0:
            count += 1
    return count

if __name__ == '__main__':
    puzzle_input = read_file(FILE)
    processed_input = lines_preprocessing(puzzle_input)
    zeros = count_zeros(processed_input)
    print(zeros)

