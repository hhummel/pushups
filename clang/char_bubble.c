#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define MAX_STRING 2501
#define NUM_STRING 50

void swap(char* i, char* j) {
    char temp[MAX_STRING];
    strcpy(temp, i);
    strcpy(i, j);
    strcpy(j, temp);
}

int compare_reverse(char* i, char* j) {
    char* a = i;
    char* b = j;

    while (a && b) {
        if (*a > *b) {
            return 1;
        }
        else if (*a < *b) {
            return 0;
        }
        else {
            a++;
            b++;
        }
    }
    return *a ? 1 : 0; 
}

int compare(char* i, char* j) {
    char* a = i;
    char* b = j;

    while (a && b) {
        if (*a < *b) {
            return 1;
        }
        else if (*a > *b) {
            return 0;
        }
        else {
            a++;
            b++;
        }
    }
    return *a ? 1 : 0; 
}

int compare_len(char* i, char* j) {
    return strlen(i) > strlen(j);
}

int compare_len_reverse(char* i, char* j) {
    return strlen(i) < strlen(j);
}

void print_output(char** a) {
    for (int i=0; i<10; i++) {
        printf("%s\n", a[i]);
    }
    printf("\n");
}

int main() {
    const char* tmp[] = {"abc", "hic", "the", "source", "is", "satan", "is", "a", "jokey", "phrase"};

    char array[50][2500];
    for (int i=0; i<10; i++) {
        strncpy(array[i], tmp[i], MAX_STRING);
    }
/*
    char** a;
    a = malloc(NUM_STRING * sizeof(char*));
    for (int i; i < NUM_STRING; i++) {
        a[i] = malloc(MAX_STRING * sizeof(char));
    }
    for (int i=0; i<10; i++) {
        strncpy(array[i], tmp[i], MAX_STRING);
    }
*/

    //print_output(a);

    for (int i=0; i<10; i++) {
        printf("%s\n", array[i]);
    }
    printf("\n");

    int (*fun_ptr)(char*, char*);
    fun_ptr = &compare_reverse;
    for (int i=0; i<10; i++) {
        for (int j=0; j<i; j++) {
            if ((*fun_ptr)(array[i], array[j])) {
                swap(array[i], array[j]);
            }
        }
    }

    fun_ptr = &compare_len;
    for (int i=0; i<10; i++) {
        for (int j=0; j<i; j++) {
            if ((*fun_ptr)(array[i], array[j])) {
                swap(array[i], array[j]);
            }
        }
    }

    for (int i=0; i<10; i++) {
        printf("%s\n", array[i]);
    }
    printf("\n");

    return 0;
}

