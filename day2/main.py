class GameSet:
    def __init__(self, game_id: int):
        self.id = game_id
        self.red = 0
        self.blue = 0
        self.green = 0

    def check_max(self, color: str, count: int):
        if color == "red" and self.red < count:
            self.red = count
        if color == "blue" and self.blue < count:
            self.blue = count
        if color == "green" and self.green < count:
            self.green = count

    def is_valid(self):
        if self.red <= 12 and self.green <= 13 and self.blue <= 14:
            return True

        return False

    def get_bag_info(self, bags_arr: list[str]):
        for bag in bags_arr:
            bag_arr = bag.strip().split(" ")
            self.check_max(bag_arr[1], int(bag_arr[0]))


def read_lines(path: str):
    lines = []
    f = open(path, "r")
    for line in f:
        if line != "":
            line = line.strip()
            lines.append(line)

    return lines


def format_lines(lines: list[str]):
    formatted_input = []

    for line in lines:
        line = line.removeprefix("Game").strip()
        line_arr = line.split(":")
        formatted_input.append(line_arr)

    return formatted_input


def main():
    lines = read_lines("./input.txt")
    input_arr = format_lines(lines)
    games_arr = []
    output_sum = 0

    for game in input_arr:
        game_set = GameSet(int(game[0]))
        rounds = game[1].split(";")

        for game_round in rounds:
            bags_arr = game_round.split(",")
            game_set.get_bag_info(bags_arr)

        games_arr.append(game_set)

    for game in games_arr:
        if game.is_valid():
            output_sum = output_sum + game.id

    print(output_sum)


if __name__ == "__main__":
    main()
