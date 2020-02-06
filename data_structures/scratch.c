#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

char* kth_word_in_mth_sentence_of_nth_paragraph(char**** document, int k, int m, int n) {

}

char** kth_sentence_in_mth_paragraph(char**** document, int k, int m) { 

}

char*** kth_paragraph(char**** document, int k) {

}

int clear_buf(char* buffer) {
    char* b_ptr = buffer;
    while (*b_ptr != '\0') {
        *b_ptr++ = '\0';
    }
    return 0;
}

int resize_doc(int words, int sentences, int paras, char* dimension, char**** document){
    switch(*dimension) {
        case 'w':
            document[paras][sentences] = (char**)realloc(document[paras][sentences], (words + 1) * sizeof(char*));
            break;
        case 's':
            document[paras] = (char***)realloc(document[paras], (sentences + 1) * sizeof(char**));
            break;
        case 'p':
            document = (char****)realloc(document, (paras + 1) * sizeof(char***));
    }
    return 0;
}

int set_word(int char_index, int word_index, int sentence_index, int para_index, char* buffer, char**** document){
    char* word = (char*)malloc(char_index * sizeof(char));
    strcpy(word, buffer);
    document[para_index][sentence_index][word_index] = word;
    printf("In set word: %s\n", word);
    clear_buf(buffer);
    return 0;
}

char**** get_document(char* text) {
    char* ptr = text;
    char buffer [1000] = {'\0'};
    int char_index = 0;
    int word_index = 0;
    int sentence_index = 0;
    int para_index = 0;
    char**** document;
    document = (char****)malloc(sizeof(char****));
    document[0] = (char***)malloc(sizeof(char***));
    document[0][0] = (char**)malloc(sizeof(char**));
    document[0][0][0] = (char*)malloc(sizeof(char*));

    while(*ptr != EOF) {
        switch(*ptr) {
            case ' ':
                printf("Here at space\n");
                resize_doc(word_index, sentence_index, para_index, "w", document);
                set_word(char_index, word_index, sentence_index, para_index, buffer, document);
                char_index = 0;
                word_index++;
                break;
            case '.':
                printf("Here at .\n");
                resize_doc(word_index, sentence_index, para_index, "w", document);
                set_word(char_index, word_index, sentence_index, para_index, buffer, document);
                resize_doc(word_index, sentence_index, para_index, "s", document);
                char_index = 0;
                word_index = 0;
                sentence_index++;
                if (*(ptr + 1) == ' ') {
                    ptr++;
                }
                break;
            case '\n':
                printf("Here at newline\n");
                resize_doc(word_index, sentence_index, para_index, "p", document);
                sentence_index = 0;
                para_index++;
                break;
            case '\0':
                printf("Here at null\n");
                return document;
                break;
            default:
                printf("Here reading %c\n", *ptr);
                buffer[char_index++] = *ptr;
        }
        ptr++;
    }
}

int main() {
    char* string = "The Cat in the Hat is a well known classic. It is funny. There are many other books for children. Like Harry Potter.\nThey are good to read with kids.";
    get_document(string);
}
