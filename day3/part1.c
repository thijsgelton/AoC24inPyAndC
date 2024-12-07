#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>

#define MAX_LINE_LENGTH 1000 // Max length of each line in the input file

// Function to multiply two integers
int mul(int x1, int x2)
{
    return x1 * x2;
}

// Function to extract numbers from a "mul(x, y)" string and multiply them
int process_mul_match(char *mul_str)
{
    int x1, x2;
    // Parsing the string to extract numbers inside "mul(x, y)"
    sscanf(mul_str, "mul(%d,%d)", &x1, &x2);
    return mul(x1, x2); // Call mul() to get the product
}

int main()
{
    FILE *file = fopen("input.txt", "r");
    if (file == NULL)
    {
        perror("Failed to open file");
        return 1; // Return error code if file can't be opened
    }

    char line[MAX_LINE_LENGTH]; // Buffer to store each line from the file
    int sum = 0;                // This will store the sum of all products

    // Regex pattern to match "mul(x, y)" where x and y are digits
    regex_t regex;
    const char *pattern = "mul\\([0-9]{1,3},[0-9]{1,3}\\)"; // Pattern for mul(x, y)

    // Compile the regular expression
    if (regcomp(&regex, pattern, REG_EXTENDED) != 0)
    {
        perror("Failed to compile regex");
        fclose(file);
        return 1; // Return error code if regex fails to compile
    }

    // Read the entire file into a string
    char input_str[MAX_LINE_LENGTH * 10]; // Adjust size based on expected file content
    input_str[0] = '\0';                  // Initialize the string as empty
    while (fgets(line, sizeof(line), file))
    {
        strcat(input_str, line); // Append each line to the input string
    }

    fclose(file); // Close the file after reading

    // Use regex to find all "mul(x, y)" occurrences in the input string
    regmatch_t match;
    char *ptr = input_str; // Pointer to traverse through the input string

    // Loop through all the matches found by the regex
    while (regexec(&regex, ptr, 1, &match, 0) == 0)
    {
        // Extract the substring for the current match
        char match_str[match.rm_eo - match.rm_so + 1];
        strncpy(match_str, ptr + match.rm_so, match.rm_eo - match.rm_so);
        match_str[match.rm_eo - match.rm_so] = '\0'; // Null-terminate the substring

        // Process the match and add the result to the sum
        sum += process_mul_match(match_str);

        // Move the pointer to continue searching after the current match
        ptr += match.rm_eo;
    }

    // Free the memory used by the regex object
    regfree(&regex);

    // Output the final sum
    printf("Sum of all products: %d\n", sum);

    return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>

#define MAX_LINE_LENGTH 1000 // Max length of each line in the input file

// Function to multiply two integers
int mul(int x1, int x2)
{
    return x1 * x2;
}

// Function to extract numbers from a "mul(x, y)" string and multiply them
int process_mul_match(char *mul_str)
{
    int x1, x2;
    // Parsing the string to extract numbers inside "mul(x, y)"
    sscanf(mul_str, "mul(%d,%d)", &x1, &x2);
    return mul(x1, x2); // Call mul() to get the product
}

int main()
{
    FILE *file = fopen("input.txt", "r");
    if (file == NULL)
    {
        perror("Failed to open file");
        return 1; // Return error code if file can't be opened
    }

    char line[MAX_LINE_LENGTH]; // Buffer to store each line from the file
    int sum = 0;                // This will store the sum of all products

    // Regex pattern to match "mul(x, y)" where x and y are digits
    regex_t regex;
    const char *pattern = "mul\\([0-9]{1,3},[0-9]{1,3}\\)"; // Pattern for mul(x, y)

    // Compile the regular expression
    if (regcomp(&regex, pattern, REG_EXTENDED) != 0)
    {
        perror("Failed to compile regex");
        fclose(file);
        return 1; // Return error code if regex fails to compile
    }

    // Read the entire file into a string
    char input_str[MAX_LINE_LENGTH * 10]; // Adjust size based on expected file content
    input_str[0] = '\0';                  // Initialize the string as empty
    while (fgets(line, sizeof(line), file))
    {
        strcat(input_str, line); // Append each line to the input string
    }

    fclose(file); // Close the file after reading

    // Use regex to find all "mul(x, y)" occurrences in the input string
    regmatch_t match;
    char *ptr = input_str; // Pointer to traverse through the input string

    // Loop through all the matches found by the regex
    while (regexec(&regex, ptr, 1, &match, 0) == 0)
    {
        // Extract the substring for the current match
        char match_str[match.rm_eo - match.rm_so + 1];
        strncpy(match_str, ptr + match.rm_so, match.rm_eo - match.rm_so);
        match_str[match.rm_eo - match.rm_so] = '\0'; // Null-terminate the substring

        // Process the match and add the result to the sum
        sum += process_mul_match(match_str);

        // Move the pointer to continue searching after the current match
        ptr += match.rm_eo;
    }

    // Free the memory used by the regex object
    regfree(&regex);

    // Output the final sum
    printf("Sum of all products: %d\n", sum);

    return 0;
}
