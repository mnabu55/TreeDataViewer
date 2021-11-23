class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_left(self, node):
        self.left_child = node

    def add_right(self, node):
        self.right_child = node

    def __str__(self):
        left_value = self.left_child.value if self.left_child is not None else "None"
        right_value = self.right_child.value if self.right_child is not None else "None"
        return "{}: {} {}".format(self.value, left_value, right_value)


def main():
    A = BinaryNode("A")
    B = BinaryNode("B")
    C = BinaryNode("C")
    D = BinaryNode("D")
    E = BinaryNode("E")
    F = BinaryNode("F")
    Root = BinaryNode("Root")
    Root.add_left(A)
    Root.add_right(B)
    A.add_left(C)
    A.add_right(D)
    B.add_right(E)
    E.add_left(F)

    print(Root)
    print(A)
    print(B)
    print(C)
    print(D)
    print(E)
    print(F)


if __name__ == "__main__":
    main()
