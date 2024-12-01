#include <stdio.h>
#include <stdlib.h>

int count_occurrences(int arr[], int size, int value) {
    int count = 0;
    for(int i = 0; i < size; i++) {
        if(arr[i] == value) {
            count++;
        }
    }
    return count;
}


int main() {
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        perror("Failed to open file");
        return 1;
    }

    int left[1000], right[1000];
    int size = 0;

    // Read input file and parse values into left and right arrays
    while(fscanf(file, " %d %d", &left[size], &right[size]) != EOF) {
        size++;
    }
    fclose(file);

    int total_similarity = 0;
    for(int i = 0; i < size; i++) {
        total_similarity = total_similarity + left[i] * count_occurrences(right, size, left[i]);

    }
    printf("%d\n", total_similarity);
    return 0;
}