class Race:

    def __init__(self, time: int, distance: int):
        self.time = time
        self.distance = distance

    def get_possibility_sum(self):
        possibility_sum = 0

        for i in range(self.time):
            speed = i
            time_left = self.time - i
            my_distance = speed * time_left
            if my_distance > self.distance:
                possibility_sum = possibility_sum + 1

        if possibility_sum == 0:
            possibility_sum = 1

        return possibility_sum


def read_lines(path):
    lines = []
    f = open(path, "r")
    for line in f:
        if line != "":
            lines.append(" ".join(line.split(":")[1].split()).strip())

    return lines


# for part 1
def prepare_races(lines: list[str]):
    races = []
    times = lines[0].split(" ")
    distances = lines[1].split(" ")
    length = len(times)

    for i in range(length):
        time = int(times[i])
        distance = int(distances[i])
        race = Race(time, distance)
        races.append(race)

    return races


# for part 2
def prepare_race(lines: list[str]):
    time = lines[0].replace(" ", "")
    distance = lines[1].replace(" ", "")

    return Race(int(time), int(distance))


def main():
    output = 1
    lines = read_lines("./input.txt")
    # part 1
    """"
    races = prepare_races(lines)
    
    for race in races:
        output = output * race.get_possibility_sum()
    """
    # part 2
    race = prepare_race(lines)

    output = output * race.get_possibility_sum()

    print(output)


if __name__ == "__main__":
    main()
