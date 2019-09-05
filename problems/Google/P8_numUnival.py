class Node:
    def __init__(self,
                 val,
                 left=None,
                 right=None):
        self.val = val
        self.left = left
        self.right = right

class Problem8(object):

    def __init__(self,
                 name):
        self.name = name

    def solver_num_unival(self, root):
        num_unival = [0]

        def traverse(node, num_unival):
            if node is None:
                return True

            left_if = traverse(node.left, num_unival)
            right_if = traverse(node.right, num_unival)

            if (not left_if) or (not right_if):
                return False

            if node.left and not (node.val == node.left.val):
                return False

            if node.right and not (node.val == node.right.val):
                return False

            num_unival[0] += 1
            return True

        traverse(root, num_unival)

        return num_unival[0]

    def __repr__(self):
        return "Problem #8 [Easy]: " + self.name + "\nThis problem was asked by Google"

if __name__ == '__main__':
    p = Problem8('Given a binary tree, find the number of unival subtrees')
    print(p)

    x1 = Node(0,
            left=Node(1),
            right=Node(0,
                left=Node(1,
                    left=Node(1),
                    right=Node(1)
                    ),
                right=Node(0)
                ),
            )

    x2 = Node(5,
            left=Node(4,
                left=Node(4),
                right=Node(4),
                ),
            right=Node(5,
                left=None,
                right=Node(4),
                ),
            )

    unival = getattr(p, 'solver_num_unival')
    print("Solution from solver for number of unival subtrees (inp 1): {}".format(unival(x1)))
    print("Solution from solver for number of unival subtrees (inp 2): {}".format(unival(x2)))
