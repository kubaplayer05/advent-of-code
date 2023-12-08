class NetworkNode:

    def __init__(self, name: str, left: str, right: str, index: int):
        self.name = name
        self.left = left
        self.right = right
        self.index = index


def read_lines(path):
    lines = []
    f = open(path, "r")
    for line in f:
        if line.strip() != "":
            lines.append(line.strip())

    return lines


def prepare_nodes(nodes_arr: list[str]):
    nodes = []

    for i, node in enumerate(nodes_arr):
        name = node.split("=")[0].strip()
        rl = node.split("=")[1].strip()
        left = rl.split(",")[0].removeprefix("(").strip()
        right = rl.split(",")[1].removesuffix(")").strip()
        nodes.append(NetworkNode(name, left, right, i))

    return nodes


def find_node(nodes: list[NetworkNode], node_name: str):
    for i in range(len(nodes)):
        if nodes[i].name == node_name:
            return i

    return -1


def find_starting_nodes(nodes: list[NetworkNode]):
    starting_nodes = []

    for node in nodes:
        if node.name.endswith("A"):
            starting_nodes.append(node)

    return starting_nodes


def get_steps_count(starting_node: NetworkNode, sequence: str, nodes: list[NetworkNode]):
    actual_node = starting_node.name
    actual_index = starting_node.index
    steps = 0
    sequence_index = 0
    sequence_length = len(sequence)

    while actual_node.endswith("Z") is False:
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


def get_steps_lmc(steps: list[int]):
    steps_lmc = steps[0]

    for i in range(1, len(steps)):
        num1 = steps_lmc
        num2 = steps[i]

        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        gcd = num1
        steps_lmc = (steps_lmc * steps[i]) // gcd

    return steps_lmc


def main():
    lines = read_lines("./input.txt")
    sequence = lines[0]
    nodes_str = lines[1:]
    nodes = prepare_nodes(nodes_str)

    starting_nodes = find_starting_nodes(nodes)
    nodes_steps = []

    for node in starting_nodes:
        step = get_steps_count(node, sequence, nodes)
        nodes_steps.append(step)

    print(nodes_steps)

    lmc = get_steps_lmc(nodes_steps)

    print(lmc)


if __name__ == "__main__":
    main()
