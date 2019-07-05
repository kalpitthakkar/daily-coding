class Node:
    def __init__(self,
                 val,
                 left=None,
                 right=None):
        self.val = val
        self.left = left
        self.right = right

class Problem3(object):

    def __init__(self,
                 name):
        self.name = name

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
    
    def solver(self, func):
        return getattr(self, func)

    def __repr__(self):
        return "Problem #3 [Medium]: " + self.name + "\nThis problem was asked by Google"

if __name__ == '__main__':
    p = Problem3('Serialize and Deserialize a binary tree into string and tree respectively')
    print(p)

    x = Node('root',
            Node('left',
            Node('left.left')),
            Node('right'))
    print(x)

    serialize = getattr(p,'serialize')
    deserialize = getattr(p,'deserialize')

    serialized_tree = p.solver('serialize')(x)
    print("Solution from solver for serialization: {}".format(serialized_tree))
    deserialized_root = p.solver('deserialize')(serialized_tree)
    print("Solution from solver for deserialization: {}".format(deserialized_root.left.left.val))

    print("The testcase given in the question: assert deserialize(serialize(node)).left.left.val == 'left.left'.\n" +
        "Evaluation using our code: {}".format(deserialize(serialize(x)).left.left.val == 'left.left'))
