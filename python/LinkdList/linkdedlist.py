# Linked List Structure:

#     Node: Each node will have two parts:
#         data: The value stored in the node.
#         next: A reference to the next node in the list.

#     LinkedList: The linked list will manage the nodes and provide methods to:
#         Insert nodes.
#         Delete nodes.
#         Print the linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current = self.head
            while current.next: # Traverse to last node
                current = current.next
            # Set the current node's next to the new node
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        # print("None")

    def delete(self, data):
        current = self.head
        previous = None

        # Case 1: The node to be deleted is the head
        if current and current.data == data:
            self.head = current.next  # Move head to the next node
            current = None  # Delete the node
            return

        # Case 2: Search for the node to be deleted
        while current and current.data != data:
            previous = current
            current = current.next

        # Case 3: Node not found
        if current is None:
            print(f"Node with data {data} not found!")
            return

        # Case 4: Node found, remove it
        previous.next = current.next  # Bypass the node to delete it
        current = None  # Delete the node

# Example usage
if __name__ == "__main__":
    # Create a linked list
    ll = LinkedList()

    # Append data to the linked list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)

    print("Linked List after appending values:")
    ll.print_list()  # Output: 10 -> 20 -> 30 -> 40 -> None

    # Delete a node with value 20
    ll.delete(20)
    print("Linked List after deleting value 20:")
    ll.print_list()  # Output: 10 -> 30 -> 40 -> None

    # Delete a node with value 50 (non-existent)
    print("Linked List after deleting value 10:")
    ll.delete(10)  # Output: Node with data 50 not found!
    ll.print_list()  # Output: 10 -> 30 -> 40 -> None
