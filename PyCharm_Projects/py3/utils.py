import os
#### https://stackabuse.com/python-linked-lists/

def removeDuplicatesFromList(list):
    return list(dict.fromkeys(list))


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def output_list(self):
        "outputs the list (the value of the node, actually)"
        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            # jump to the linked node
            current_node = current_node.next

        return

    def unordered_search(self, value):
        "search the linked list for the node that has this value"

        # define current_node
        current_node = self.head

        # define position
        node_id = 1

        # define list of results
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1

        return results

class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
        self.next = None
    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

node1 = Node(15)
node2 = Node(8.2)
item3 = "Berlin"
node4 = Node(15)

track = SingleLinkedList()
print("track length: %i" % track.list_length())

for current_item in [node1, node2, item3]:
    track.append(current_item)
    print("track length: %i" % track.list_length())
track.output_list()
print(track.head.value, track.tail.value)