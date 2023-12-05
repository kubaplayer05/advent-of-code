class Scratchcard:

    def __init__(self, wining_n: list, your_n: list):
        self.wining_n = wining_n
        self.your_n = your_n

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
    for line in f:
        if line != "":
            scratch = line.split(":")[1].split("|")
            winning_n = scratch[0].strip().split(" ")
            your_n = (' '.join(scratch[1].split()).split(" "))
            scratchcard = Scratchcard(winning_n, your_n)
            scratchcards.append(scratchcard)

    return scratchcards


def main():
    scratchcards = read_lines("./input.txt")
    output_sum = 0

    for card in scratchcards:
        points_from_card = card.get_points()
        output_sum = output_sum + points_from_card

    print(output_sum)


if __name__ == "__main__":
    main()
