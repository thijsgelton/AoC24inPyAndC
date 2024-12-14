import numpy as np


def check_up(i_r, j_c, current_letter, input_matrix):
    antinode_positions = []
    for i in range(i_r - 1, -1, -1):
        if input_matrix[i, j_c] == current_letter:
            dist = abs(i_r - i)
            for x in range(150):
                antinode_pos = (i - dist * x, j_c)
                antinode_positions.append((antinode_pos, j_c))
    return antinode_positions


def check_down(i_r, j_c, current_letter, input_matrix):
    antinode_positions = []
    for i in range(i_r + 1, h):  # Check if this is correct later
        if input_matrix[i, j_c] == current_letter:
            dist = abs(i_r - i)
            for x in range(150):
                antinode_pos = (i + dist * x, j_c)
                antinode_positions.append((antinode_pos, j_c))
    return antinode_positions


def check_left(i_r, j_c, current_letter, input_matrix):
    antinode_positions = []
    for j in range(j_c - 1, -1, -1):
        if input_matrix[i_r, j] == current_letter:
            dist = abs(j_c - j)
            for x in range(150):
                antinode_pos = (i_r, j - dist * x)
                antinode_positions.append((i_r, antinode_pos))
    return antinode_positions


def check_right(i_r, j_c, current_letter, input_matrix):
    antinode_positions = []
    for j in range(j_c + 1, w):
        if input_matrix[i_r, j] == current_letter:
            dist = abs(j_c - j)
            for x in range(150):
                antinode_pos = (i_r, j + dist * x)
                antinode_positions.append((i_r, antinode_pos))
    return antinode_positions


def check_up_left(i_r, j_c, current_letter, input_matrix):
    antinode_positions = []
    for i in range(i_r - 1, -1, -1):
        for j in range(j_c - 1, -1, -1):
            if input_matrix[i, j] == current_letter:
                dist_i = abs(i_r - i)
                dist_j = abs(j_c - j)
                for x in range(150):
                    antinode_pos = (i - dist_i * x, j - dist_j * x)
                    antinode_positions.append(antinode_pos)
    return antinode_positions


def check_up_right(i_r, j_c, current_letter, input_matrix):
    antinode_positions = []
    for i in range(i_r - 1, -1, -1):
        for j in range(j_c + 1, w):
            if input_matrix[i, j] == current_letter:
                dist_i = abs(i_r - i)
                dist_j = abs(j_c - j)
                for x in range(150):
                    antinode_pos = (i - dist_i * x, j + dist_j * x)
                    antinode_positions.append(antinode_pos)
    return antinode_positions


def check_down_left(i_r, j_c, current_letter, input_matrix):
    antinode_positions = []
    for i in range(i_r + 1, h):
        for j in range(j_c - 1, -1, -1):
            if input_matrix[i, j] == current_letter:
                dist_i = abs(i_r - i)
                dist_j = abs(j_c - j)
                for x in range(150):
                    antinode_pos = (i + dist_i * x, j - dist_j * x)
                    antinode_positions.append(antinode_pos)
    return antinode_positions


def check_down_right(i_r, j_c, current_letter, input_matrix):
    antinode_positions = []
    for i in range(i_r + 1, h):
        for j in range(j_c + 1, w):
            if input_matrix[i, j] == current_letter:
                dist_i = abs(i_r - i)
                dist_j = abs(j_c - j)
                for x in range(150):
                    antinode_pos = (i + dist_i * x, j + dist_j * x)
                    antinode_positions.append(antinode_pos)
    return antinode_positions


def remove_outside_map(antinode_positions):
    correct = []
    for pos in antinode_positions:
        if not (pos[0] < 0 or pos[0] > h - 1 or pos[1] < 0 or pos[1] > w - 1):
            correct.append(pos)
    return correct


if __name__ == "__main__":

    with open(r"C:\Users\thijs\Programming\AoC24inPyAndC\day8\input.txt") as f:
        input_matrix = np.array([list(l.strip()) for l in f.readlines()])
        output_matrix = np.copy(
            input_matrix
        )  # In this matrix we can override any letter, even if it is an antenna
        h, w = input_matrix.shape
        for i_r in range(w):
            for j_c in range(h):
                current_letter = input_matrix[i_r, j_c]
                antinode_positions = []
                if input_matrix[i_r, j_c] == ".":
                    continue
                antinode_positions += check_up(i_r, j_c, current_letter, input_matrix)
                antinode_positions += check_down(i_r, j_c, current_letter, input_matrix)
                antinode_positions += check_left(i_r, j_c, current_letter, input_matrix)
                antinode_positions += check_right(
                    i_r, j_c, current_letter, input_matrix
                )
                antinode_positions += check_up_left(
                    i_r, j_c, current_letter, input_matrix
                )
                antinode_positions += check_up_right(
                    i_r, j_c, current_letter, input_matrix
                )
                antinode_positions += check_down_left(
                    i_r, j_c, current_letter, input_matrix
                )
                antinode_positions += check_down_right(
                    i_r, j_c, current_letter, input_matrix
                )
                antinode_positions = remove_outside_map(antinode_positions)
                for antinode_position in antinode_positions:
                    output_matrix[*antinode_position] = "#"
        with open("output.txt", "w") as f:
            for l in output_matrix:
                f.write("".join(l) + "\n")
        print(len(output_matrix[output_matrix == "#"]))
