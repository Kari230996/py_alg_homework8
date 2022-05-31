'''
Практическая работа 8

Деревья. Хэш-функция
'''

# 2. Закодируйте любую строку по алгоритму Хаффмана.
# Превратите строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.


from collections import Counter


def dict_check(text):
    result = dict()

    for line in txt:
        line = line.lower()
        for i in line:
            if i in result:
                result[i] += 1
            else:
                result.update({i: 1})
    return result

txt = input('Введите текст: ')


class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None


class Huffman(object):
    def __init__(self, char_weights):
        self.Leaf = [Node(k, v) for k, v in char_weights.items()]

        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node: node.value, reverse=True)
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.left = self.Leaf.pop(-1)
            n.right = self.Leaf.pop(-1)
            self.Leaf.append(n)

        self.root = self.Leaf[0]
        self.Buffer = list(range(10))


    def generate(self, tree, length):

        node = tree

        if not node:
            return
        elif node.name:
            print(node.name + ": ", end='')

            for i in range(length):
                print(self.Buffer[i], end='')
            print('\n')
            return


        self.Buffer[length] = 0
        self.generate(node.left, length + 1)
        self.Buffer[length] = 1
        self.generate(node.right, length + 1)

    def get_code(self):
        self.generate(self.root, 0)


if __name__ == '__main__':
    result = dict_check(txt)
    tree = Huffman(result)
    tree.get_code()


