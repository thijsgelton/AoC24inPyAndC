import numpy as np

with open("input.txt") as f:
    input_matrix = np.array([list(l.strip()) for l in f.readlines()])
    w, h = input_matrix.shape
    count = 0
    output_matrix = np.zeros((h, w)).astype(int).astype(str)
    for j in range(w):
        for i in range(h):
            if (
                input_matrix[i][j] == "A"
                and i >= 1
                and j >= 1
                and i < h - 1
                and j < w - 1
            ):
                if (
                    np.array([input_matrix[i + k, j + k] for k in range(-1, 2)])
                    == ["M", "A", "S"]
                ).all() and (
                    np.array([input_matrix[i + k, j - k] for k in range(-1, 2)])
                    == ["M", "A", "S"]
                ).all():
                    count += 1
                    for k in range(-1, 2):
                        output_matrix[i + k, j - k] = input_matrix[i + k, j - k]
                        output_matrix[i + k, j + k] = input_matrix[i + k, j + k]
                if (
                    np.array([input_matrix[i - k, j + k] for k in range(-1, 2)])
                    == ["M", "A", "S"]
                ).all() and (
                    np.array([input_matrix[i - k, j - k] for k in range(-1, 2)])
                    == ["M", "A", "S"]
                ).all():
                    count += 1
                    for k in range(-1, 2):
                        output_matrix[i + k, j - k] = input_matrix[i + k, j - k]
                        output_matrix[i + k, j + k] = input_matrix[i + k, j + k]
                if (
                    np.array([input_matrix[i - k, j - k] for k in range(-1, 2)])
                    == ["M", "A", "S"]
                ).all() and (
                    np.array([input_matrix[i + k, j - k] for k in range(-1, 2)])
                    == ["M", "A", "S"]
                ).all():
                    count += 1
                    for k in range(-1, 2):
                        output_matrix[i + k, j - k] = input_matrix[i + k, j - k]
                        output_matrix[i + k, j + k] = input_matrix[i + k, j + k]

                if (
                    np.array([input_matrix[i - k, j + k] for k in range(-1, 2)])
                    == ["M", "A", "S"]
                ).all() and (
                    np.array([input_matrix[i + k, j + k] for k in range(-1, 2)])
                    == ["M", "A", "S"]
                ).all():
                    count += 1
                    for k in range(-1, 2):
                        output_matrix[i + k, j - k] = input_matrix[i + k, j - k]
                        output_matrix[i + k, j + k] = input_matrix[i + k, j + k]
    print(output_matrix)
    print(count)
