def read_lines(path):
    lines = []
    f = open(path, "r")
    for line in f:
        if line != "":
            lines.append(line)

    return lines


def check_if_contains(line: str, start_index: int, end_index: int, get_smaller: bool):
    digit_arr = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    checked_str = line[start_index:end_index]

    actual_index = -1
    value = -1

    for i in range(len(digit_arr)):
        x = checked_str.find(digit_arr[i])

        if actual_index == -1 and x != -1:
            actual_index = x
            value = i + 1
            continue

        if actual_index != -1 and get_smaller and x != -1 and x < actual_index:
            actual_index = x
            value = i + 1
            continue

        if actual_index != -1 and get_smaller is False and x > actual_index and x != -1:
            actual_index = x
            value = i + 1
            continue

    return [value, actual_index]


def main():
    input_arr = read_lines("./input.txt")
    print(len(input_arr))
    digits = []
    my_sum = 0

    for index, word in enumerate(input_arr):
        first = -1
        second = -1
        i = 0
        j = len(word) - 1

        while (first == -1 or second == -1) and i <= j:
            if first == -1 and word[i].isdigit():
                first = word[i]

            if second == -1 and word[j].isdigit():
                second = word[j]

            if first == -1:
                i += 1
            if second == -1:
                j -= 1

        if first == -1:
            i = len(word)

        first_arr = check_if_contains(word, 0, i, True)
        first_val = first_arr[0]

        if second == -1:
            j = first_arr[1]

        last_arr = check_if_contains(word, j, len(word), False)
        last_val = last_arr[0]

        if first_val != -1:
            first = first_val

        if last_val != -1:
            second = last_val

        if last_val == -1 and second == -1:
            second = first_val

        digit = str(first) + str(second)
        print(digit)
        digits.append(int(digit))

    for digit in digits:
        my_sum += digit

    print(my_sum)


if __name__ == "__main__":
    main()
