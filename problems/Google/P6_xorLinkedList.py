class Node(object):
    def __init__(self,
                 val=None,
                 xoraddress=None):
        self.val = val
        self.both = xoraddress

class Problem6(object):

    def __init__(self,
                 name):
        self.name = name

    def add(self, head, element):
        while(not head is None):
            addr_next = xor_address(get_pointer(head.both), None)
            

        new_node = Node()
        new_node.val = element
        new_node.both = xor_address(get_pointer(head), None)

    def __repr__(self):
        return "Problem #6 [Hard]: " + self.name + "\nThis problem was asked by Google"

if __name__ == '__main__':
    p = Problem6('Implement a XOR linked list')
    print(p)
