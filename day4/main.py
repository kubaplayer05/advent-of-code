class Scratchcard:

    def __init__(self, wining_n: list, your_n: list, card_number: int):
        self.wining_n = wining_n
        self.your_n = your_n
        self.number = card_number
        self.copies = []
        self.checked = False

    def get_copies_numbers(self):

        copies = []
        points = 0

        for n in self.your_n:
            if n in self.wining_n:
                points += 1

        for i in range(points):
            copies.append(self.number + i + 1)

        self.copies = copies
        self.checked = True
        return copies

    def get_points(self):
        points = 0

        for n in self.your_n:
            if n in self.wining_n:
                if points == 0:
                    points = 1
                else:
                    points = points * 2

        return points


def read_lines(path):
    scratchcards = []
    f = open(path, "r")
    for i, line in enumerate(f):
        if line != "":
            scratch = line.split(":")[1].split("|")
            winning_n = scratch[0].strip().split(" ")
            your_n = (' '.join(scratch[1].split()).split(" "))
            scratchcard = Scratchcard(winning_n, your_n, i + 1)
            scratchcards.append(scratchcard)

    return scratchcards


def check_if_all_checked(scratchcards: list[Scratchcard]):
    for scratchcard in scratchcards:
        if scratchcard.checked is False:
            return False

    return True


def main():
    scratchcards = read_lines("./input.txt")
    my_scratchcards = scratchcards.copy()
    all_scratchcards = []
    output_sum = 0
    checked = False

    for scratchcard in my_scratchcards:
        if scratchcard.checked is False:
            all_scratchcards.append(scratchcard)
            won_copies = scratchcard.get_copies_numbers()

            for copy_index in won_copies:
                scratchcard_copy = Scratchcard(scratchcards[copy_index - 1].wining_n,
                                               scratchcards[copy_index - 1].your_n, copy_index)

                all_scratchcards.append(scratchcard_copy)

    while checked is False:

        checked = True

        for scratchcard in all_scratchcards:
            if scratchcard.checked is False:
                checked = False

                won_copies = scratchcard.get_copies_numbers()

                for copy_index in won_copies:
                    scratchcard_copy = Scratchcard(scratchcards[copy_index - 1].wining_n,
                                                   scratchcards[copy_index - 1].your_n, copy_index)

                    all_scratchcards.append(scratchcard_copy)

    print(len(all_scratchcards))


if __name__ == "__main__":
    main()
