# Linked list example


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        """
        It inserts a new node at the head of the list.
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, value):
        """
        If finds the node by the value.
        """
        item = self.head
        while item != None:
            if item.get_data() == value:
                return item
            else:
                item = item.get_next()
        return None

    def delete_at_index(self, index):
        if index < self.count - 1:
            return

        if index == 0:
            self.head = self.head.get_next()
        else:
            temp_index = 0
            node = self.head
            while temp_index < index - 1:
                node = node.get_next()
                temp_index += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        temp_node = self.head
        while temp_node != None:
            print(f"Node: {temp_node.get_data()}")
            temp_node = temp_node.get_next()

    # create a linked list and insert some items


item_list = LinkedList()
item_list.insert(38)
item_list.insert(49)
item_list.insert(13)
item_list.insert(15)
item_list.dump_list()

# exercise the list
print("Item count: ", item_list.get_count())
print("Finding item: ", item_list.find(13))
print("Finding item: ", item_list.find(78))

# delete an item
# item_list.delete_at_index(3)
# print("Item count: ", item_list.get_count())
# print("Finding item: ", item_list.find(38))
# item_list.dump_list()
