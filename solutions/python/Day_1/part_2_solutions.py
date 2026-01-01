file_path = "./puzzle.txt"

instructions = [x.strip("\n") for x in open(file_path).readlines()]

current_position = 50


def move_left(current_position, steps):
    actual_steps = abs(steps) % 100
    landing_position = current_position - actual_steps
    if landing_position < 0:
        landing_position = 100 - abs(landing_position)
    return landing_position


def move_right(current_position, steps):
    actual_steps = abs(steps) % 100
    landing_position = current_position + steps
    if landing_position > 99:
        difference = landing_position % 100
        landing_position = difference
    return landing_position


def parse_instruction(instruction):
    movement = instruction[0]
    steps = int(instruction[1:])
    return movement, steps


key = 0

for instruction in instructions:
    movement, steps = parse_instruction(instruction)
    for step in range(steps):
        if movement == "L":
            landing_position = move_left(current_position, 1)
        else:
            landing_position = move_right(current_position, 1)

        current_position = landing_position
        print(f"The Dial is rotated {instruction} to point to {landing_position}")
        if landing_position == 0:
            key += 1


print("Key: ", key)
