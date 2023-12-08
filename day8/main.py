class NetworkNode:

    def __init__(self, name: str, left: str, right: str):
        self.name = name
        self.left = left
        self.right = right


def read_lines(path):
    lines = []
    f = open(path, "r")
    for line in f:
        if line.strip() != "":
            lines.append(line.strip())

    return lines


def prepare_nodes(nodes_arr: list[str]):
    nodes = []

    for node in nodes_arr:
        name = node.split("=")[0].strip()
        rl = node.split("=")[1].strip()
        left = rl.split(",")[0].removeprefix("(").strip()
        right = rl.split(",")[1].removesuffix(")").strip()
        nodes.append(NetworkNode(name, left, right))

    return nodes


def find_node(nodes: list[NetworkNode], node_name: str):
    for i in range(len(nodes)):
        if nodes[i].name == node_name:
            return i

    return -1


def get_steps_count(sequence: str, nodes: list[NetworkNode]):
    actual_node = "AAA"
    actual_index = find_node(nodes, actual_node)
    steps = 0
    sequence_index = 0
    sequence_length = len(sequence)

    while actual_node != "ZZZ":
        steps += 1
        move = sequence[sequence_index]

        if move == "L":
            actual_node = nodes[actual_index].left

        if move == "R":
            actual_node = nodes[actual_index].right

        actual_index = find_node(nodes, actual_node)

        sequence_index += 1

        if sequence_index > sequence_length - 1:
            sequence_index = 0

    return steps


def main():
    lines = read_lines("./input.txt")
    sequence = lines[0]
    nodes_str = lines[1:]
    nodes = prepare_nodes(nodes_str)
    steps = get_steps_count(sequence, nodes)

    print(steps)


if __name__ == "__main__":
    main()
