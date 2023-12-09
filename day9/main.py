def read_lines(path):
    lines = []
    f = open(path, "r")
    for line in f:
        if line != "":
            lines.append(line.strip())

    return lines


def prepare_sequence(lines: list[str]):
    sequences = []

    for line in lines:
        sequence = []
        for digit in line.split(" "):
            sequence.append(int(digit))

        sequences.append(sequence)

    return sequences


def get_next_sequence(sequence: list):
    new_sequence = []

    for i in range(len(sequence) - 1):
        new_sequence.append(sequence[i + 1] - sequence[i])

    return new_sequence


def check_if_zero(sequence: list[int]):
    for digit in sequence:
        if digit != 0:
            return False

    return True


def get_next_value(sequence: list[int]):
    value = 0
    actual_index = 0
    history_sequence = [sequence]

    while check_if_zero(history_sequence[actual_index]) is False:
        new_sequence = get_next_sequence(history_sequence[actual_index])
        history_sequence.append(new_sequence)
        actual_index += 1

    history_sequence[actual_index].append(0)

    while actual_index != 0:
        actual_sequence = history_sequence[actual_index]
        previous_sequence = history_sequence[actual_index - 1]

        num1 = actual_sequence[len(actual_sequence) - 1]
        num2 = previous_sequence[len(previous_sequence) - 1]

        value = num1 + num2

        previous_sequence.append(value)

        actual_index -= 1

    return value


def main():
    value_sum = 0
    lines = read_lines("./input.txt")
    sequences = prepare_sequence(lines)

    for sequence in sequences:
        value = get_next_value(sequence)
        value_sum += value

    print(value_sum)


if __name__ == "__main__":
    main()
