import sys
sys.path.append("../..")
from central import Solver

class Node:
    def __init__(self,
                 val,
                 left=None,
                 right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(Solver):

    def __init__(self,
                 pnum,
                 desc,
                 company,
                 category,
                 level,
                 logging=True):
        
        super(Solution, self).__init__(
            pnum, desc, company, category, level,
            logging
        )

    def serialize(self, root):
        serial_string = ""
        depth = 0

        def traverse(node, serial_string, depth):
            if node is None:
                serial_string += "None"
                return serial_string

            serial_string += str(node.val)+","
            serial_string = traverse(node.left, serial_string, depth+1)
            serial_string += ","
            serial_string = traverse(node.right, serial_string, depth+1)

            return serial_string

        serial_string = traverse(root, serial_string, depth)

        return serial_string

    def deserialize(self, string):
        
        def traverse(node, tree_string, idx):
            if idx >= len(tree_string):
                return idx, node

            if 'None' in tree_string[idx]:
                return idx, node

            node = Node(tree_string[idx])
            idx, node.left = traverse(node.left, tree_string, idx+1)
            idx, node.right = traverse(node.right, tree_string, idx+1)

            return idx, node

        root = Node('dummy')
        tree_string = string.split(',')
        _, root = traverse(root, tree_string, 0)
        return root
    
    def solve(self, x, **kwargs):
        func = kwargs['func']

        return getattr(self, func)(x)

    def interpret(self, x, **kwargs):
        # TODO: Implement this
        return

if __name__ == '__main__':
    desc=("Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.\n\n" +
         "For example, given the following Node class\n\n" +

          "class Node:\n" +
          "    def __init__(self, val, left=None, right=None):\n" +
          "        self.val = val\n" +
          "        self.left = left\n" +
          "        self.right = right\n\n" +
          
          "The following test should pass:\n\n" +

          "node = Node('root', Node('left', Node('left.left')), Node('right'))\n" +
          "assert deserialize(serialize(node)).left.left.val == 'left.left')\n\n")
    
    p = Solution(
        pnum=3,
        desc=desc,
        company="Google",
        category="Tree,String Manipulation",
        level="Medium",
        logging=False
    )
    p.print_description()

    x = Node('root',
            Node('left',
            Node('left.left')),
            Node('right'))

    solver = p._get_solver()

    print("Test example:\n" +
          "Node('root', Node('left', Node('left.left')), Node('right'))\n\n")

    serialized_tree = solver(x, func='serialize')
    print("Solution from solver for serialization: {}".format(serialized_tree))
    deserialized_root = solver(serialized_tree, func='deserialize')
    print("Solution from solver for deserialization (printing root.left.left.val): {}".format(deserialized_root.left.left.val))

    print("The testcase given in the question: assert deserialize(serialize(node)).left.left.val == 'left.left'.\n" +
        "Evaluation using our code: {}".format(solver(solver(x, func='serialize'), func='deserialize').left.left.val == 'left.left'))

    if p.logging:
        interpreter = p._get_interpreter()
        interpreter(x, func='serialize')
        interpreter(serialized_tree, func='deserialize')
