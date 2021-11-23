from typing import List


class NaryNode:
    '''A class to represent a nary node.
    '''
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def add_child(self, node) -> None:
        self.children.append(node)

    def __str__(self) -> str:
        return f"{self.value}: " + " ".join([str(x.value) for x in self.children])


def main():
    Root = NaryNode("Root")
    A = NaryNode("A")
    B = NaryNode("B")
    C = NaryNode("C")
    D = NaryNode("D")
    E = NaryNode("E")
    F = NaryNode("F")
    G = NaryNode("G")
    H = NaryNode("H")
    I = NaryNode("I")
    Root.add_child(A)
    Root.add_child(B)
    Root.add_child(C)
    A.add_child(D)
    A.add_child(E)
    C.add_child(F)
    D.add_child(G)
    F.add_child(H)
    F.add_child(I)

    print(Root)
    print(A)
    print(B)
    print(C)
    print(D)
    print(E)
    print(F)
    print(G)
    print(H)
    print(I)


if __name__ == "__main__":
    main()
