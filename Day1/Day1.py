FILE = "example.txt"

def read_file(file_input):
    with open(file_input, 'r') as file:
        lines = file.readlines()
    for x, line in enumerate(lines):
        lines[x] = line.strip('\n')
    return lines

if __name__ == '__main__':
    puzzle_input = read_file(FILE)
    print(puzzle_input)

