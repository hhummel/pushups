#include <stdlib.h>
#include <stdio.h>

int array[10] = {3, 2, 4, 5, 1, 6, 8, 0, 9, 7};

void swap(int* i, int* j) {
    int temp = *i;
    *i = *j;
    *j = temp;
}

int compare_reverse(int* i, int* j){
    if (*i > *j) {
        return 1;
    }
    return 0;
}

int compare(int* i, int* j){
    if (*i < *j) {
        return 1;
    }
    return 0;
}

void main() {
    int (*fun_ptr)(int*, int*);
    fun_ptr = &compare;
    for (int i=0; i<10; i++) {
        for (int j=0; j<i; j++) {
            if ((*fun_ptr)(&array[i], &array[j])) {
                swap(&array[i], &array[j]);
            }
        }
    }

    for (int i=0; i<10; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    fun_ptr = &compare_reverse;
    for (int i=0; i<10; i++) {
        for (int j=0; j<i; j++) {
            if ((*fun_ptr)(&array[i], &array[j])) {
                swap(&array[i], &array[j]);
            }
        }
    }

    for (int i=0; i<10; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

