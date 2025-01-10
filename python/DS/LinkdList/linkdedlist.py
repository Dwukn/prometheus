# # Linked List Structure:

# #     Node: Each node will have two parts:
# #         data: The value stored in the node.
# #         next: A reference to the next node in the list.

# #     LinkedList: The linked list will manage the nodes and provide methods to:
# #         Insert nodes.
# #         Delete nodes.
# #         Print the linked list.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         self.head = new_node
#         new_node.next = self.head

#     def print_list(self):
#         if self.head is None:
#             print("List is empty")
#             return
#         itr = self.head
#         llstr=''
#         while itr:
#             llstr += str(itr.data) + '-->'
#             itr = itr.next
#         print(llstr)

#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             current = self.head
#             while current.next: # Traverse to last node
#                 current = current.next
#             # Set the current node's next to the new node
#             current.next = new_node

#     # def print_list(self):
#     #     current = self.head
#     #     while current:
#     #         print(current.data)
#     #         current = current.next
#     #     # print("None")

#     def delete(self, data):
#         current = self.head
#         previous = None

#         # Case 1: The node to be deleted is the head
#         if current and current.data == data:
#             self.head = current.next  # Move head to the next node
#             current = None  # Delete the node
#             return

#         # Case 2: Search for the node to be deleted
#         while current and current.data != data:
#             previous = current
#             current = current.next

#         # Case 3: Node not found
#         if current is None:
#             print(f"Node with data {data} not found!")
#             return

#         # Case 4: Node found, remove it
#         previous.next = current.next  # Bypass the node to delete it
#         current = None  # Delete the node

# # Example usage
# if __name__ == "__main__":
#     # Create a linked list
#     ll = LinkedList()

#     # Append data to the linked list
#     ll.append(10)
#     ll.append(20)
#     ll.append(30)
#     ll.append(40)
#     ll.insert_at_beginning(5)

#     print("Linked List after appending values:")
#     ll.print_list()  # Output: 10 -> 20 -> 30 -> 40 -> None

#     # Delete a node with value 20
#     ll.delete(20)
#     print("Linked List after deleting value 20:")
#     ll.print_list()  # Output: 10 -> 30 -> 40 -> None

#     # Delete a node with value 50 (non-existent)
#     print("Linked List after deleting value 10:")
#     ll.delete(10)  # Output: Node with data 50 not found!
#     ll.print_list()  # Output: 10 -> 30 -> 40 -> None

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def append(self,data): # Add a new node to the end of the linked list
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current = self.head
            while current.next: # Traverse to last node
                current = current.next
            # Set the current node's next to the new node
            current.next = new_node
    def insert(self,index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.insert_at_beginning(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def remove(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def insert_values(self, data_list):
        for data in data_list:
            self.append(data)

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return
        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break
            itr=itr.next
    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            itr=itr.next
    def replace(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        count=0
        itr=self.head
        while itr:
            if count==index:
                itr.data=data
                break
            itr=itr.next
            count+=1

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    for i in range(1,5):
        ll.append(i)
    ll.print()
    ll.replace(2,100)
    ll.insert_values(["banana","apple","mango"])
    ll.insert_after_value("banana","orange")
    ll.remove_by_value("apple")
    ll.insert(0,'start')
    ll.replace(2,100)
    ll.append(30)
    ll.print()
