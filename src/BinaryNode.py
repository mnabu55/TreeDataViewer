class BinaryNode:
    '''A class to represent a binary node.
    '''
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left_child = left
        self.right_child = right

    def add_left(self, node) -> None:
        self.left_child = node

    def add_right(self, node) -> None:
        self.right_child = node

    def __str__(self) -> str:
        left_value = self.left_child.value if self.left_child is not None else "None"
        right_value = self.right_child.value if self.right_child is not None else "None"
        return f"{self.value}: {left_value} {right_value}"


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
