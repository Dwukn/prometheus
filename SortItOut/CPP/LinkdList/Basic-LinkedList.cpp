#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

Node* head = nullptr;

// Insert at the beginning
void Insert(int data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}

// Delete the first node
void Delete() {
    if (head == nullptr) return;  // Empty list, nothing to delete
    Node* temp = head;
    head = head->next;
    delete temp;
}

// Print the list
void Print() {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    Insert(10);
    Insert(20);
    Insert(30);

    cout << "List: ";
    Print();

    Delete(); // Remove the first node (10)

    cout << "List after deletion: ";
    Print();

    return 0;
}
