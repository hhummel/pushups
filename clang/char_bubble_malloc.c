#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_STRING 2501
#define NUM_STRING 50
    
typedef int (*FUN_PTR)(char*, char*);

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
    return *a ? 0 : 1; 
}

int count_distinct(char* i) {
    int len = strlen(i) + 1;
    char* buf = malloc(len * sizeof(char));
    buf[0] = '\0';
    for (int j=0; j<len; j++) {
        int k = 0;
        while (buf[k] !='\0' && buf[k] !=i[j]) {
            k++;
        }
        if (buf[k] == '\0') {
            buf[k] = i[j];
            buf[k+1] = '\0';
        }
    }
    return strlen(buf);
}

int compare_distinct(char* i, char* j) {
    int count_i = count_distinct(i);
    int count_j = count_distinct(j);
   
    if (count_i < count_j){
        return 1;
    } else if (count_i > count_j){
        return 0;
    } else {
        return compare(i, j);
    }

}

int compare_len(char* i, char* j) {
    int str_i = strlen(i);
    int str_j = strlen(j);
    if (str_i < str_j) {
        return 1;
    } else if (str_i > str_j) {
        return 0;
    } else {
        return compare(i, j);
    }
}

int compare_len_reverse(char* i, char* j) {
    return strlen(i) < strlen(j);
}

void print_output(char** a) {
    for (int i=0; i<22; i++) {
        printf("%s\n", a[i]);
    }
    printf("\n");
}

void sort_array(char** a, const int len, FUN_PTR ptr) {
    for (int i=1; i<len; i++) {
        for (int j=0; j<i; j++) {
            if ((*ptr)(a[i], a[j])) {
                swap(a[i], a[j]);
            }
        }
    }
}

int main() {

    const char* tmp[] = {
        "hjzzwdq",
        "upsovufynjgyndaslodyexwlgxmfbdtxunmphtq",
        "ewwrcyknmnnsmmetjsamvvkriyhrrznyvjpxjznvpcobouw",
        "mwmkrydbwmsqlhohsdgbftxwylzohyovudf",
        "bjryxmojteqmhypmumkszkgiiveea",
        "ubwmzuypdttvhd",
        "xrnl",
        "hnmovwlbalnxmjlodjfiebdmezlvoyzwlnkjjvkmi",
        "jujukofsxltazxbkuqjumw",
        "yhtvshdtsz",
        "okrvcqgxsgwusqkbmyawwhrrbyuvstz",
        "fsbjihgbpcvivhljfnfdvyuyyqtqlvwtnzcwjlx",
        "puikbwuijbl",
        "affaxariv",
        "bjpghyreygahrbdnjm",
        "utqbaryak",
        "wzkhoqomhulpuuivxvglmcgcdgvdhflffvmvnckwwxm",
        "runqsvbexiicqghxlsesqqqds",
        "cqxoiqkxgcshgrrrvixchkxmf",
        "evszvupu",
        "akvxqxqzgjtxfdwjmggylvfgo",
        "divztvjqtbnldtuwsbbolnx"
    };

    char** a;
    a = malloc(NUM_STRING * sizeof(char*));
    for (int i=0; i < NUM_STRING; i++) {
        a[i] = malloc(MAX_STRING * sizeof(char));
    }

    for (int i=0; i<22; i++) {
        strcpy(a[i], tmp[i]);
    }

    print_output(a);

    //Sort
    sort_array(a, 22, &compare);
    print_output(a);

    //Reverse
    sort_array(a, 22, &compare_reverse);
    print_output(a);

    //By length and then lex
    sort_array(a, 22, &compare_len);
    print_output(a);

    //By distinct and then lex
    sort_array(a, 22, &compare_distinct);
    print_output(a);

    return 0;
}

