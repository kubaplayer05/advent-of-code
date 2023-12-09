class NumberPos:

    def __init__(self, number: int, indexes: list[int]):
        self.number = number
        self.indexes = indexes

    def is_part_number(self, symbols_indexes: list[list[int]], line: int, max_lines: int):

        arr_length = len(self.indexes)

        if line == 0:
            for arr_index in range(arr_length):
                if arr_index == 0 and arr_length > 1 and (self.indexes[0] in symbols_indexes[0]
                                                          or self.indexes[0] - 1 in symbols_indexes[0]
                                                          or self.indexes[0] in symbols_indexes[1]
                                                          or self.indexes[0] - 1 in symbols_indexes[1]):
                    return True

                if arr_index == arr_length - 1 and arr_length > 1 and (self.indexes[arr_index] in symbols_indexes[0]
                                                                       or self.indexes[arr_index] + 1 in
                                                                       symbols_indexes[0]
                                                                       or self.indexes[arr_index] in symbols_indexes[1]
                                                                       or self.indexes[arr_index] + 1 in
                                                                       symbols_indexes[1]):
                    return True

                if (self.indexes[arr_index] in symbols_indexes[0]
                        or self.indexes[arr_index] in symbols_indexes[1]
                        or self.indexes[arr_index] - 1 in symbols_indexes[0]
                        or self.indexes[arr_index] - 1 in symbols_indexes[1]
                        or self.indexes[arr_index] + 1 in symbols_indexes[0]
                        or self.indexes[arr_index] + 1 in symbols_indexes[1]):
                    return True
                else:
                    continue
        else:

            if line == max_lines:
                for arr_index in range(arr_length):
                    if arr_index == 0 and arr_length > 1 and (self.indexes[0] in symbols_indexes[max_lines]
                                                              or self.indexes[0] - 1 in symbols_indexes[max_lines]
                                                              or self.indexes[0] in symbols_indexes[max_lines - 1]
                                                              or self.indexes[0] - 1 in symbols_indexes[max_lines - 1]):
                        return True

                    if arr_index == arr_length - 1 and arr_length > 1 and (
                            self.indexes[arr_index] in symbols_indexes[max_lines]
                            or self.indexes[arr_index] + 1 in symbols_indexes[max_lines]
                            or self.indexes[arr_index] in symbols_indexes[max_lines - 1]
                            or self.indexes[arr_index] + 1 in symbols_indexes[max_lines - 1]):
                        return True

                    if (self.indexes[arr_index] in symbols_indexes[max_lines]
                            or self.indexes[arr_index] in symbols_indexes[max_lines - 1]
                            or self.indexes[arr_index] - 1 in symbols_indexes[max_lines]
                            or self.indexes[arr_index] - 1 in symbols_indexes[max_lines - 1]
                            or self.indexes[arr_index] + 1 in symbols_indexes[max_lines]
                            or self.indexes[arr_index] + 1 in symbols_indexes[max_lines - 1]):
                        return True
                    else:
                        continue

            else:

                for arr_index in range(arr_length):
                    if arr_index == 0 and arr_length > 1 and (self.indexes[0] in symbols_indexes[line]
                                                              or self.indexes[0] - 1 in symbols_indexes[line]
                                                              or self.indexes[0] in symbols_indexes[line - 1]
                                                              or self.indexes[0] - 1 in symbols_indexes[line - 1]
                                                              or self.indexes[0] in symbols_indexes[line + 1]
                                                              or self.indexes[0] - 1 in symbols_indexes[line + 1]):
                        return True

                    if arr_index == arr_length - 1 and arr_length > 1 and (
                            self.indexes[arr_index] in symbols_indexes[line]
                            or self.indexes[arr_index] + 1 in symbols_indexes[
                                line]
                            or self.indexes[arr_index] in symbols_indexes[
                                line - 1]
                            or self.indexes[arr_index] + 1 in symbols_indexes[
                                line - 1]
                            or self.indexes[arr_index] in symbols_indexes[
                                line + 1]
                            or self.indexes[arr_index] + 1 in symbols_indexes[
                                line + 1]):
                        return True

                    if (self.indexes[arr_index] in symbols_indexes[line]
                            or self.indexes[arr_index] in symbols_indexes[line - 1]
                            or self.indexes[arr_index] in symbols_indexes[line + 1]
                            or self.indexes[arr_index] - 1 in symbols_indexes[line - 1]
                            or self.indexes[arr_index] - 1 in symbols_indexes[line]
                            or self.indexes[arr_index] - 1 in symbols_indexes[line + 1]
                            or self.indexes[arr_index] + 1 in symbols_indexes[line - 1]
                            or self.indexes[arr_index] + 1 in symbols_indexes[line]
                            or self.indexes[arr_index] + 1 in symbols_indexes[line + 1]):
                        return True

                return False


def read_lines(path):
    lines = []
    f = open(path, "r")
    for line in f:
        if line != "":
            lines.append(line.rstrip())

    return lines


def get_line_info(line: str):
    actual_number = ""
    actual_indexes = []
    symbols_indexes = []
    gear_indexes = []
    numbers_pos = []
    length = len(line)

    for i in range(length):

        char = line[i]

        if char.isdigit():
            actual_number = actual_number + char
            actual_indexes.append(i)

        if char.isdigit() is False and actual_number != "" or (char.isdigit() and i == length - 1):
            numbers_pos.append(NumberPos(int(actual_number), actual_indexes))
            actual_number = ""
            actual_indexes = []

        if char == "*":
            gear_indexes.append(i)
            continue

        if char.isdigit() is False and char != ".":
            symbols_indexes.append(i)

    return [numbers_pos, symbols_indexes, gear_indexes]


def check_lines(numbers_pos, symbols_indexes):
    partial_numbers = []
    print(symbols_indexes)

    for line_index in range(len(numbers_pos)):

        number_line_pos = numbers_pos[line_index]

        for pos in range(len(number_line_pos)):
            if number_line_pos[pos].is_part_number(symbols_indexes, line_index, len(numbers_pos) - 1):
                partial_numbers.append(number_line_pos[pos].number)
                print(number_line_pos[pos].number)

    return partial_numbers


def get_gear_ratio(gear_index: int, line_index: int, numbers_pos: list[list[NumberPos]]):
    length = len(numbers_pos)
    connected_numbers = []

    for number in numbers_pos[line_index]:
        if gear_index - 1 in number.indexes or gear_index + 1 in number.indexes:
            connected_numbers.append(number)

    if line_index != 0:
        for number in numbers_pos[line_index - 1]:
            if gear_index - 1 in number.indexes or gear_index + 1 in number.indexes or gear_index in number.indexes:
                connected_numbers.append(number)

    if line_index != length - 1:
        for number in numbers_pos[line_index + 1]:
            if gear_index - 1 in number.indexes or gear_index + 1 in number.indexes or gear_index in number.indexes:
                connected_numbers.append(number)

    count = len(connected_numbers)

    if count != 2:
        return 0

    return connected_numbers[0].number * connected_numbers[1].number


def get_all_gears_ratio(gears_pos: list[list[int]], numbers_pos: list[list[NumberPos]]):
    ratio = 0

    for line_index, gear_pos in enumerate(gears_pos):
        for gear_index in gear_pos:
            value = get_gear_ratio(gear_index, line_index, numbers_pos)
            ratio += value

    return ratio


def main():
    lines = read_lines("./input.txt")
    symbols_indexes = []
    numbers_pos = []
    gears_pos = []
    partial_numbers = []
    output_sum = 0

    """ part 1
    for line in lines:
        line_info = get_line_info(line)
        numbers_pos.append(line_info[0])
        symbols_indexes.append(line_info[1])

    partial_numbers = check_lines(numbers_pos, symbols_indexes)

    for number in partial_numbers:
        output_sum = output_sum + int(number)

    print(output_sum)
    """

    for line in lines:
        line_info = get_line_info(line)
        numbers_pos.append(line_info[0])
        gears_pos.append(line_info[2])

    ratio = get_all_gears_ratio(gears_pos, numbers_pos)
    print(ratio)


if __name__ == "__main__":
    main()
