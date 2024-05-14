# 1 method to implement linked list

class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

node1 = LinkedListNode("3")
node2 = LinkedListNode("7")
node3 = LinkedListNode("10")

node1.next_node = node2  # node1 -> node2, "3" -> "7"
node2.next_node = node3  # node2 -> node3, "7" -> "10"

# "3" -> "7" -> "10"

current_node = node1
while True:
    print(current_node.value, "->", end=' ')
    if current_node.next_node is None:
        print("None")
        break
    current_node = current_node.next_node

# 2 way to implement linked list (more functionality)

class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return

        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def print_linked_list(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end=" ")
            currentNode = currentNode.nextNode
        print("None")

ll = LinkedList()
ll.print_linked_list()
ll.insert("3")
ll.print_linked_list()
ll.insert("44")
ll.print_linked_list()
ll.insert("55")
ll.print_linked_list()
