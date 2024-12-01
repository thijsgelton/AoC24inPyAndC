#include <stdio.h>
#include <stdlib.h>

// Function to compare two integers for qsort
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
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
    while (fscanf(file, "%d %d", &left[size], &right[size]) != EOF) {
        size++;
    }
    fclose(file);

    // Sort both arrays
    qsort(left, size, sizeof(int), compare);
    qsort(right, size, sizeof(int), compare);

    // Calculate total distance
    int total_distance = 0;
    for (int i = 0; i < size; i++) {
        total_distance += abs(left[i] - right[i]);
    }

    printf("Total Distance: %d\n", total_distance);
    return 0;
}
