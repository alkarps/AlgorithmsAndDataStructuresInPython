# Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter


def test_encode_haffman(fun):
    assert "000000100010000101010000001100110001010100000010001001111111" == fun("beep boop beer!")
    assert "001110110010001001010111111101010000001001000001" == fun("Hello World!")


class Node:
    def __init__(self, frequency, char=None, left=None, right=None):
        self.frequency = frequency
        self.char = char
        self.left = left
        self.right = right
        left_height = 0 if left is None else (left.height + 1)
        right_height = 0 if right is None else (right.height + 1)
        self.height = 0 + max(left_height, right_height)

    def __str__(self):
        result = '{"char":' + (f'"{self.char}"' if self.char is not None else "null")
        result += ',"frequency":"' + str(self.frequency) + '","left":'
        result += (f"{self.left}" if self.left is not None else "null") + ',"right":'
        result += (f"{self.right}" if self.right is not None else "null") + '}'
        return result


def __str_as_tree(data):
    nodes = [Node(x[1], x[0]) for x in Counter(data).items()]
    while len(nodes) != 1:
        first = nodes.pop(0)
        second = nodes.pop(0)
        nodes.append(Node(frequency=first.frequency + second.frequency, left=first, right=second))
        nodes = sorted(nodes, key=lambda item: item.frequency)
    return nodes[0]


def __tree_to_map_of_codes(node, image, height=None):
    maps = {}
    if node.height == 0:
        maps[node.char] = image
    else:
        if height is None:
            height = node.height - 1
        maps.update(__tree_to_map_of_codes(node.left, image, height - 1))
        image = image[:height] + "1" + image[height + 1:]
        maps.update(__tree_to_map_of_codes(node.right, image, height - 1))
    return maps


def encode_haffman(data, pretty_print=False):
    assert data is not None, 'Ошибка ввода данных. Ожидается строка длиной больше 0'
    assert type(data) == str, 'Ошибка ввода данных. Ожидается строка длиной больше 0'
    assert len(data) > 0, 'Ошибка ввода данных. Ожидается строка длиной больше 0'
    tree = __str_as_tree(data)
    map_of_codes = __tree_to_map_of_codes(tree, "0" * tree.height)
    encoded_data = (" " if pretty_print else "").join(map(lambda x: map_of_codes[x], data))
    return encoded_data


if __name__ == "__main__":
    test_encode_haffman(encode_haffman)
    print(encode_haffman("The book of the generation of Jesus Christ, the son of David, the son of Abraham", True))
