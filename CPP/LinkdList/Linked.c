#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node* next;
};
struct Node* head = NULL;

void Insert(int x){
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    // *temp.data = x; // This is wrong because temp is a pointer to a struct, not a struct
    // (*temp).next = head; // This is correct but the arrow operator is more readable
    temp->data = x;
    temp->next = head;
    head = temp;
    // free(temp); // this is wrong as you are freeing the memory of the node you just inserted
}
void Print(){
    struct Node* temp = head; // This is a pointer to a struct
    printf("List is: ");
    while(temp != NULL){ // Initialized a while loop   //In C++, this would be while(temp != nullptr)
        printf("%d ", temp->data); // prints the data of the current node
        temp = temp->next; // Move poiner to the next node
    }
    printf("\n");
}

// Function to free the memory of all nodes
void FreeList(){
    struct Node* temp = head;
    while(temp != NULL){
        struct Node* nextNode = temp->next;
        free(temp);
        temp = nextNode;
    }
}

int main(){
    int n,i, x;
    printf("How many numbers?\n");
    scanf("%d", &n); // reads the number of elements
    for(i = 0; i < n; i++){
        printf("Enter the number\n");
        scanf("%d", &x);
        Insert(x); // Insert element in the list
        Print(); // Print the list
    }
    FreeList();
}
