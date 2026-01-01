from helpers import (
    get_instructions,
    parse_instruction,
    move_left,
    move_right,
    get_formatted_output,
)


def main():
    file_path = "./sample_puzzle.txt"
    current_position = 50
    instructions = get_instructions(file_path)
    key = 0

    for instruction in instructions:
        movement, steps = parse_instruction(instruction)
        for step in range(steps):
            if movement == "L":
                landing_position = move_left(current_position, 1)
            else:
                landing_position = move_right(current_position, 1)

            current_position = landing_position
            formatted_output = get_formatted_output(instruction, landing_position)
            print(formatted_output)
            if landing_position == 0:
                key += 1

    print("Key: ", key)


main()
