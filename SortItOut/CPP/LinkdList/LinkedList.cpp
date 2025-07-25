#include <iostream> // This includes the input/output library to use cout and cin
using namespace std;

// Structure to represent a node in a linked list
struct Node {
    int data;   // Data to store the value
    Node* next; // Pointer to the next node in the list
};

// Declare the head of the list, initially set to nullptr (empty list)
Node* head = nullptr;

// Function to insert a node at a given position in the list
void Insert(int data, int pos) {
    // Allocate memory for a new node and assign the data to it
    Node* temp1 = new Node();
    temp1->data = data;
    temp1->next = nullptr; // Set the next pointer to null (because it's a new node)

    // Special case: Inserting at the beginning of the list (position 1)
    if (pos == 1) {
        temp1->next = head;  // Point the new node to the current head
        head = temp1;        // Update the head to the new node
        return;              // Done, no further action needed
    }

    // Traverse the list to find the (pos-1)th node (the node before the insert position)
    Node* temp2 = head;
    int currentPosition = 1;  // Start from position 1 (the head)
    while (temp2 != nullptr && currentPosition < pos - 1) {
        temp2 = temp2->next;  // Move to the next node
        currentPosition++;    // Increment the position
    }

    // If we reached the end and couldn't insert at the desired position, it's out of bounds
    if (temp2 == nullptr) {
        cout << "Error: Position out of bounds!" << endl; // Display error message
        delete temp1;  // Clean up memory for the new node since we won't use it
        return;
    }

    // Insert the new node at the desired position
    temp1->next = temp2->next; // The new node's next will be the old node's next
    temp2->next = temp1;       // The old node's next now points to the new node
}

// Function to print the entire list
void Print() {
    Node* temp = head;  // Start at the head of the list
    while (temp != nullptr) {  // Traverse until we reach the end of the list
        cout << temp->data << " "; // Print the data of the current node
        temp = temp->next;         // Move to the next node in the list
    }
    cout << endl;  // After printing all the nodes, print a newline
}

// Function to free (delete) all the nodes in the list to prevent memory leaks
void FreeList() {
    Node* temp = head;  // Start at the head of the list
    while (temp != nullptr) {  // Traverse until we reach the end of the list
        Node* nextNode = temp->next;  // Save the address of the next node
        delete temp;  // Deallocate the current node's memory
        temp = nextNode;  // Move to the next node
    }
}

// Function to delete a node at a specific position in the list
void Delete(int pos) {
    // Special case: If position is 0 or less, we return because it’s an invalid position
    if (pos == 0){
        return;
    }

    // Special case: Deleting the first node (head of the list)
    if (pos == 1) {
        Node* temp = head;   // Save the head node to delete it
        head = head->next;   // Move the head to the next node
        delete temp;         // Deallocate the memory for the original head
        return;
    }

    // Traverse the list to find the (pos-1)th node (the node before the one we want to delete)
    Node* temp = head;
    int currentPosition = 1;
    while (temp != nullptr && currentPosition < pos - 1) {
        temp = temp->next;  // Move to the next node
        currentPosition++;  // Increment the position
    }

    // If we reached the end or position is out of bounds, display an error message
    if (temp == nullptr || temp->next == nullptr) {
        cout << "Error: Position out of bounds!" << endl;  // Print an error message
        return;
    }

    // The node to delete is temp->next
    Node* nodeToDelete = temp->next;    // Save the node to delete
    temp->next = nodeToDelete->next;     // Bypass the node to delete in the list
    delete nodeToDelete;                // Free the memory for the deleted node
}

// Function to reverse the linked list
void Reverse() {
    Node* current = head;  // Start at the head of the list
    Node* prev = nullptr;  // This will eventually point to the new head (the last node)
    Node* next = nullptr;  // Temporary pointer to hold the next node during reversal

    // Traverse the list and reverse the direction of the links
    while (current != nullptr) {
        next = current->next; // Save the next node
        current->next = prev; // Reverse the current node's pointer
        prev = current;       // Move the prev pointer to the current node
        current = next;       // Move to the next node
    }

    // After the loop, prev points to the last node, which should be the new head
    head = prev;
}

int main() {
    int loop, i, data, pos, dpos;
    cout << "How many numbers?" << endl;
    cin >> loop;  // Read the number of elements to be inserted

    // Insert the elements and print the list after each insertion
    for (i = 0; i < loop; i++) {
        cout << "Enter the number and position" << endl;
        cin >> data >> pos; // Read the data and the position to insert
        Insert(data, pos);   // Insert the element at the given position
        Print();              // Print the current state of the list
    }

    // Ask the user for a position to delete a node
    cout << "Delete at pos: ";
    cin >> dpos;
    Delete(dpos);  // Delete the node at the specified position
    Print();       // Print the list after deletion

    Reverse();     // Reverse the list
    Print();       // Print the reversed list

    // Call FreeList to deallocate all memory used by the list
    FreeList();

    return 0;  // Program ends here
}
