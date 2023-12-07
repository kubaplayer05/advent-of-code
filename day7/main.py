class CardsHand:
    """
        [2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A] - available cards
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] - indexes

        Types of hand (lower value == weaker):
        0 - undefined
        1 - High card
        2 - One pair
        3 - Two pairs
        4 - Three of a kind
        5 - Full House
        6 - Four of a kind
        7 - Five of a kind
    """

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.type = 0

    def get_hand_type(self):
        hashmap = [0] * 13

        three_same_cards = 0
        two_same_cards = 0

        for card in self.cards:
            index = get_card_index(card)
            hashmap[index] = hashmap[index] + 1

        for card_count in hashmap:
            if card_count == 5:
                self.type = 7
                return

            if card_count == 4:
                self.type = 6
                return

            if card_count == 3:
                three_same_cards = three_same_cards + 1

            if card_count == 2:
                two_same_cards = two_same_cards + 1

        if three_same_cards == 1 and two_same_cards == 1:
            self.type = 5
            return

        if three_same_cards == 1:
            self.type = 4
            return

        if two_same_cards == 2:
            self.type = 3
            return

        if two_same_cards == 1:
            self.type = 2
            return

        self.type = 1


def read_lines(path):
    lines = []
    f = open(path, "r")
    for line in f:
        if line != "":
            lines.append(line.strip().split(" "))

    return lines


def prepare_cards(lines: list):
    cards = []

    for line in lines:
        cards.append(CardsHand(line[0], int(line[1])))

    return cards


def get_card_index(card: str):
    index = -1

    if card.isdigit():
        return int(card) - 2

    if card == "T":
        index = 8

    if card == "J":
        index = 9

    if card == "Q":
        index = 10

    if card == "K":
        index = 11

    if card == "A":
        index = 12

    return index


def merge_sort(cards_arr: list[CardsHand]):
    if len(cards_arr) > 1:

        mid = len(cards_arr) // 2
        left = cards_arr[:mid]
        right = cards_arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if compare_two_cards(left[i], right[j]):
                cards_arr[k] = right[j]
                j += 1
            else:
                cards_arr[k] = left[i]
                i += 1
            k += 1

        while i < len(left):
            cards_arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            cards_arr[k] = right[j]
            j += 1
            k += 1


def compare_two_cards(card1: CardsHand, card2: CardsHand):
    if card1.type == card2.type:
        for i in range(5):
            index1 = get_card_index(card1.cards[i])
            index2 = get_card_index(card2.cards[i])

            if index1 > index2:
                return True

            if index2 > index1:
                return False

    if card1.type > card2.type:
        return True

    return False


def main():
    output = 0
    lines = read_lines("./input.txt")
    cards = prepare_cards(lines)

    for card in cards:
        card.get_hand_type()

    merge_sort(cards)

    for i, card in enumerate(cards):
        output += card.bid * (i + 1)

    print(output)


if __name__ == "__main__":
    main()
