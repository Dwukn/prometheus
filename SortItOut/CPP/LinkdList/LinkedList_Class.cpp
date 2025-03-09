#include <iostream>
using namespace std;

// Define the structure of a node in the LinkedList
struct Node {
    int data;       // Holds the data of the node
    Node* next;     // Pointer to the next node in the list

    // Constructor to initialize the node
    Node(int value) {
        data = value;
        next = nullptr;
    }
};

// Define the class for the LinkedList
class LinkedList {
private:
    Node* head;  // Pointer to the first node of the list

public:
    // Constructor to initialize an empty list
    LinkedList() {
        head = nullptr;
    }

    // Function to add a new node at the end of the list
    void append(int value) {
        Node* newNode = new Node(value);  // Create a new node with the given value
        if (head == nullptr) {
            head = newNode;  // If the list is empty, the new node becomes the head
        } else {
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;  // Traverse to the last node
            }
            temp->next = newNode;  // Link the last node to the new node
        }
    }

    // Function to insert a new node at the beginning of the list
    void insertAtBeginning(int value) {
        Node* newNode = new Node(value);  // Create a new node with the given value
        newNode->next = head;  // Point the new node's next to the current head
        head = newNode;  // Update the head to the new node
    }

    // Function to delete the first occurrence of a value in the list
    void deleteValue(int value) {
        if (head == nullptr) {
            cout << "List is empty!" << endl;
            return;
        }

        // If the head node itself holds the value to be deleted
        if (head->data == value) {
            Node* temp = head;
            head = head->next;  // Move head to the next node
            delete temp;  // Delete the old head
            return;
        }

        // Traverse the list to find the node to delete
        Node* temp = head;
        while (temp->next != nullptr && temp->next->data != value) {
            temp = temp->next;  // Traverse to the next node
        }

        // If the value was found
        if (temp->next != nullptr) {
            Node* nodeToDelete = temp->next;
            temp->next = temp->next->next;  // Bypass the node to be deleted
            delete nodeToDelete;  // Delete the node
        } else {
            cout << "Value not found in the list!" << endl;
        }
    }

    // Function to display the list
    void display() {
        if (head == nullptr) {
            cout << "List is empty!" << endl;
            return;
        }

        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " -> ";  // Print data of the current node
            temp = temp->next;  // Move to the next node
        }
        cout << "end" << endl;  // End of the list
    }

    // Destructor to delete all nodes when the list is destroyed
    ~LinkedList() {
        Node* temp = head;
        while (temp != nullptr) {
            Node* nextNode = temp->next;
            delete temp;  // Delete the current node
            temp = nextNode;  // Move to the next node
        }
    }
};

// Main function to test the LinkedList
int main() {
    LinkedList list;

    // Adding elements to the list
    list.append(10);
    list.append(20);
    list.append(30);

    cout << "Linked List after appending elements:" << endl;
    list.display();  // Expected output: 10 -> 20 -> 30 -> nullptr

    // Inserting at the beginning
    list.insertAtBeginning(5);
    cout << "Linked List after inserting 5 at the beginning:" << endl;
    list.display();  // Expected output: 5 -> 10 -> 20 -> 30 -> nullptr

    // Deleting a value
    list.deleteValue(20);
    cout << "Linked List after deleting value 20:" << endl;
    list.display();  // Expected output: 5 -> 10 -> 30 -> nullptr

    // Deleting a value that doesn't exist
    list.deleteValue(100);  // Expected output: Value not found in the list!

    return 0;
}
