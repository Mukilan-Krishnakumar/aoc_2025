WINDOW_SIZE = 100


def get_instructions(file_path):
    instructions = [x.strip("\n") for x in open(file_path).readlines()]
    return instructions


def parse_instruction(instruction):
    movement = instruction[0]
    steps = int(instruction[1:])
    return movement, steps


def move_left(current_position, steps):
    actual_steps = abs(steps) % WINDOW_SIZE
    landing_position = current_position - actual_steps
    if landing_position < 0:
        landing_position = WINDOW_SIZE - abs(landing_position)
    return landing_position


def move_right(current_position, steps):
    actual_steps = abs(steps) % WINDOW_SIZE
    landing_position = current_position + steps
    if landing_position > WINDOW_SIZE - 1:
        difference = landing_position % WINDOW_SIZE
        landing_position = difference
    return landing_position


def get_formatted_output(instruction, landing_position):
    return f"The Dial is rotated {instruction} to point to {landing_position}"
