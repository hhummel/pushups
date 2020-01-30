#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count_distinct(const char* i) {
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

int lexicographic_sort(const char* i, const char* j) {
    if (strcmp(i, j) > 0 ) {
        return 0;
    }
    return 1;
}

int lexicographic_sort_reverse(const char* i, const char* j) {
    if (strcmp(j, i) > 0 ) {
        return 0;
    }
    return 1;
}

int sort_by_number_of_distinct_characters(const char* i, const char* j) {
    const int count_i = count_distinct(i);
    const int count_j = count_distinct(j);

    if (count_i < count_j){
        return 1;
    } else if (count_i > count_j){
        return 0;
    } else {
        return lexicographic_sort(i, j);
    }
}

int sort_by_length(const char* i, const char* j) {
    const int str_i = strlen(i);
    const int str_j = strlen(j);
    if (str_i < str_j) {
        return 1;
    } else if (str_i > str_j) {
        return 0;
    } else {
        return lexicographic_sort(i, j);;
    }
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    for (int i=1; i<len; i++) {
        for (int j=0; j<i; j++) {
            if ((*cmp_func)(arr[i], arr[j])) {
                char* temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }

    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}
