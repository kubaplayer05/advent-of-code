def read_lines(path):
    lines = []
    f = open(path, "r")
    for line in f:
        if line != "":
            lines.append(line)

    return lines


def main():
    input_arr = read_lines("./input.txt")
    digits = []
    my_sum = 0

    for index, word in enumerate(input_arr):
        first = -1
        second = -1
        i = 0
        j = len(word) - 1

        while first == -1 or second == -1:
            if first == -1 and word[i].isdigit():
                first = word[i]

            if second == -1 and word[j].isdigit():
                second = word[j]

            if first == -1:
                i += 1
            if second == -1:
                j -= 1

        digit = str(first) + str(second)
        digits.append(int(digit))

    for digit in digits:
        my_sum += digit

    print(my_sum)


if __name__ == "__main__":
    main()
