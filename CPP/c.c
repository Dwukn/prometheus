// import ctypes

// x = ctypes.c_int(29)
// print(id(x))
// print(ctypes.cast(id(x), ctypes.py_object).value)
// print(ctypes.addressof(x))
// print(x.value)
// z = 42
// print(id(z))
#include <stdio.h>
#include <stdlib.h>
void mem(){
    int var = 20;
    printf("Address of var(%d) variable: %p\n", var, &var);
}

void heap(){
    int *ptr = (int *)malloc(sizeof(int));
    *ptr = 20;
    printf("Address of var(%d) variable: %p\n", *ptr, ptr);
    free(ptr);
    printf("freed Variable: %p\n", ptr);
}
int main(){
    int x = 29;
    printf("x is '%d': %d\n", x,&x);
    // printf("%d\n", x);
    int z = 42;
    // printf("%p", &z);
    printf("z is '%d' :%p\n", z,&z);
    mem();
    heap();
    return 0;
}
