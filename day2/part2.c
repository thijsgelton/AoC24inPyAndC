#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LINE_LENGTH 1000
#define MAX_NUMBERS 20

bool is_safe(int levels[], int size)
{
    int differences[MAX_NUMBERS - 1];

    for (int i = 0; i < size - 1; i++)
    {
        differences[i] = levels[i + 1] - levels[i];
    }

    bool increasing = true;
    bool decreasing = true;
    for (int i = 0; i < size - 1; i++)
    {
        if (!(1 <= differences[i] && differences[i] <= 3))
        {
            increasing = false;
        }

        if (!(-3 <= differences[i] && differences[i] <= -1))
        {
            decreasing = false;
        }
    }
    return increasing || decreasing;
}

int main()
{
    FILE *file = fopen("input.txt", "r");
    if (file == NULL)
    {
        perror("Failed to open file");
        return 1;
    }
    char line[MAX_LINE_LENGTH];
    int count = 0;

    while (fgets(line, sizeof(line), file))
    {
        int levels[MAX_NUMBERS];
        int size = 0;

        char *token = strtok(line, " ");
        while (token != NULL)
        {
            levels[size++] = atoi(token);
            token = strtok(NULL, " ");
        }

        if (is_safe(levels, size))
        {
            count++;
        }
        else
        {
            for (int i = 0; i < size; i++)
            {
                int modified_levels[MAX_NUMBERS];
                int modified_size = 0;
                for (int j = 0; j < size; j++)
                {
                    if (j != i)
                    {
                        modified_levels[modified_size++] = levels[j];
                    }
                }
                if (is_safe(modified_levels, modified_size))
                {
                    count++;
                    break;
                }
            }
        }
    }
    fclose(file);

    printf("Count of safe lines: %d\n", count);

    return 0;
}