#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

#define MAX_ROWS 1000
#define MAX_COLS 1000

typedef enum
{
    UP,
    RIGHT,
    DOWN,
    LEFT
} Direction;

typedef struct
{
    int row;
    int col;
} Position;

char patrol_map[MAX_ROWS][MAX_COLS];
Position start_position;
Direction start_facing;
int rows, cols;

Direction directions[] = {UP, RIGHT, DOWN, LEFT};

int valid_position(Position pos)
{
    return (pos.row >= 0 && pos.row < rows && pos.col >= 0 && pos.col < cols);
}

int move_guard(Position *pos, Direction *facing)
{
    Position next_pos = *pos;
    switch (*facing)
    {
    case UP:
        next_pos.row--;
        break;
    case RIGHT:
        next_pos.col++;
        break;
    case DOWN:
        next_pos.row++;
        break;
    case LEFT:
        next_pos.col--;
        break;
    }

    if (!valid_position(next_pos) || patrol_map[next_pos.row][next_pos.col] == '#')
    {
        // Turn 90 degrees clockwise
        *facing = (*facing + 1) % 4;
        return 0;
    }
    else
    {
        *pos = next_pos;
        return 1;
    }
}

int simulate_guard(Position start_pos, Direction start_dir)
{
    Position pos = start_pos;
    Direction dir = start_dir;
    int visited[MAX_ROWS][MAX_COLS][4] = {0}; // Track visited positions with directions

    while (1)
    {
        if (visited[pos.row][pos.col][dir])
        {
            return 1; // Loop detected
        }
        visited[pos.row][pos.col][dir] = 1;

        if (!move_guard(&pos, &dir))
        {
            break; // Hit a wall or boundary
        }
    }

    return 0; // No loop detected
}

void *test_obstruction(void *arg)
{
    Position *pos = (Position *)arg;
    Position test_pos = *pos;
    char original_char = patrol_map[test_pos.row][test_pos.col];

    // Add the obstruction
    patrol_map[test_pos.row][test_pos.col] = '#';

    // Simulate guard's movement
    int loop_detected = simulate_guard(start_position, start_facing);

    // Restore the original map state
    patrol_map[test_pos.row][test_pos.col] = original_char;

    return (void *)(intptr_t)loop_detected;
}

int main()
{
    FILE *file = fopen("C:\\Users\\thijs\\Programming\\AoC24inPyAndC\\day6\\input.txt", "r");
    if (!file)
    {
        perror("Failed to open file");
        return EXIT_FAILURE;
    }

    // Read the map
    char line[MAX_COLS + 2];
    rows = 0;
    while (fgets(line, sizeof(line), file))
    {
        cols = strlen(line) - 1; // Exclude newline character
        strcpy(patrol_map[rows], line);
        for (int i = 0; i < cols; i++)
        {
            if (line[i] == '^' || line[i] == 'v' || line[i] == '<' || line[i] == '>')
            {
                start_position.row = rows;
                start_position.col = i;
                if (line[i] == '^')
                    start_facing = UP;
                else if (line[i] == '>')
                    start_facing = RIGHT;
                else if (line[i] == 'v')
                    start_facing = DOWN;
                else if (line[i] == '<')
                    start_facing = LEFT;
            }
        }
        rows++;
    }
    fclose(file);

    pthread_t threads[MAX_ROWS * MAX_COLS];
    Position positions[MAX_ROWS * MAX_COLS];
    int thread_count = 0;

    // Generate tasks for each valid empty space
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (patrol_map[i][j] == '.' && (i != start_position.row || j != start_position.col))
            {
                positions[thread_count].row = i;
                positions[thread_count].col = j;
                pthread_create(&threads[thread_count], NULL, test_obstruction, (void *)&positions[thread_count]);
                thread_count++;
            }
        }
    }

    int valid_positions = 0;

    // Join all threads and count valid obstruction positions
    for (int i = 0; i < thread_count; i++)
    {
        void *result;
        pthread_join(threads[i], &result);
        if ((intptr_t)result == 1)
        {
            valid_positions++;
        }
    }

    printf("Number of valid obstruction positions: %d\n", valid_positions);
    return EXIT_SUCCESS;
}
