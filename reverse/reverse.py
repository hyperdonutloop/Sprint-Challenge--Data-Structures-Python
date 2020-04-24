class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # if there is no node
        if node is None:
            # return nothing
            return
        # otherwise
        else:
            # if there is no next node
            if node.next_node is None:
                # current node I am on = head
                self.head = node
                # making the reference to the next node the previous
                node.next_node = prev
                # returns that value
                return

            # assigning new_node to the next node
            new_node = node.next_node
            # changing the next pointer to be previous
            node.next_node = prev
            # calls the function again (recursive magic) on the node that I am on, passing in the new_node and node
            self.reverse_list(new_node, node)
