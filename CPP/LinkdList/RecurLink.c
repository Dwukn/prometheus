#include <stdio.h>
#include <stdlib.h>

// Define the structure for the linked list node
struct Node {
    int data;          // Holds the data for the node
    struct Node* next; // Pointer to the next node in the list
};

// Declare a global pointer to the head node of the linked list
struct Node* head = NULL;

// Function to print the linked list using recursion
void Print(struct Node* p) {
    // Base case: If the current node is NULL, stop the recursion
    if (p == NULL) return;

    // Print the data of the current node
    printf("%d ", p->data);

    // Recursively print the rest of the linked list
    Print(p->next);
}

// Function to print the linked list in reverse order using recursion
void PrintReverse(struct Node* p) {
    // Base case: If the current node is NULL, stop the recursion
    if (p == NULL) return;

    // Recursively print the rest of the linked list first
    PrintReverse(p->next);

    // After the recursion returns, print the data of the current node
    printf("%d ", p->data);
}

// Function to reverse the linked list iteratively
void ReverseList() {
    // Initialize three pointers for reversing the list
    struct Node *current = head, *prev = NULL, *next = NULL;

    // Traverse the list and reverse the links between nodes
    while (current != NULL) {
        next = current->next;   // Store the next node temporarily
        current->next = prev;   // Reverse the current node's next pointer
        prev = current;         // Move the prev pointer forward to the current node
        current = next;         // Move the current pointer forward to the next node
    }

    // After the loop, prev will be pointing to the new head (last node)
    head = prev;  // Update the head to point to the new first node
}

// Function to insert a new node at the end of the linked list
struct Node* Insert(struct Node* head, int data) {
    // Allocate memory for a new node
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));

    // Assign the data to the new node and set its next pointer to NULL
    temp->data = data;
    temp->next = NULL;

    // If the list is empty (head is NULL), the new node becomes the head
    if (head == NULL) {
        head = temp;
    } else {
        // Otherwise, traverse the list to find the last node
        struct Node* temp1 = head;
        while (temp1->next != NULL) {
            temp1 = temp1->next; // Move to the next node
        }
        // Once the last node is found, add the new node after it
        temp1->next = temp;
    }

    // Return the head of the list (it may not change if the list was not empty)
    return head;
}

int main() {
    // Initialize the list as empty (head is NULL)
    head = Insert(head, 2); // Insert a node with data 2
    head = Insert(head, 10); // Insert a node with data 10
    head = Insert(head, 20); // Insert a node with data 20
    head = Insert(head, 30); // Insert a node with data 30

    // Print the linked list using the Print function
    printf("Linked List: \n");
    Print(head); // Print the list in order (2, 10, 20, 30)

    // Print a new line for better output formatting
    printf("\nPrinting Reversed Linked List: \n");

    // Print the linked list in reverse order using the PrintReverse function
    PrintReverse(head); // Print the list in reverse order (30, 20, 10, 2)

    // Print a new line for better output formatting
    printf("\nReversing Linked List... \n");

    // Reverse the linked list
    ReverseList(); // Reverses the list in place

    // Print the reversed linked list
    printf("Linked List after Reversing: \n");
    Print(head); // Print the list after it has been reversed (30, 20, 10, 2)
    printf("\n");

    return 0; // Return from main function
}
