import numpy as np

with open("input.txt") as f:
    input_matrix = np.array([list(l.strip()) for l in f.readlines()])
    w, h = input_matrix.shape
    count = 0
    output_matrix = np.zeros((h, w)).astype(int).astype(str)
    for j in range(w):
        for i in range(h):
            if input_matrix[i][j] == "X":
                if j < w - 3:
                    # Horizontal forwards
                    if (input_matrix[i, j + 1 : j + 4] == ["M", "A", "S"]).all():
                        print("Horizontal forwards", input_matrix[i, j + 1 : j + 4])
                        count += 1
                        output_matrix[i, j : j + 4] = input_matrix[i, j : j + 4]

                if j >= 3:
                    # Horizontal backwards
                    if (input_matrix[i, j - 3 : j] == ["S", "A", "M"]).all():
                        print("Horizontal backwards", input_matrix[i, j - 3 : j])
                        count += 1
                        output_matrix[i, j - 3 : j] = input_matrix[i, j - 3 : j]

                if i < h - 3:
                    # Vertical forwards
                    if (input_matrix[i + 1 : i + 4, j] == ["M", "A", "S"]).all():
                        print("Vertical forwards", input_matrix[i + 1 : i + 4, j])
                        count += 1
                        output_matrix[i : i + 4, j] = input_matrix[i : i + 4, j]

                if i >= 3:
                    # Vertical backwards
                    if (input_matrix[i - 3 : i, j] == ["S", "A", "M"]).all():
                        print("Vertical backwards", input_matrix[i - 3 : i, j])
                        count += 1
                        output_matrix[i - 3 : i + 1, j] = input_matrix[i - 3 : i + 1, j]

                if j < w - 3 and i < h - 3:
                    # Diagonal forwards
                    if (
                        np.array([input_matrix[i + k, j + k] for k in range(1, 4)])
                        == ["M", "A", "S"]
                    ).all():
                        print(
                            "Diagonal top left to bottom right",
                            np.array([input_matrix[i + k, j + k] for k in range(1, 4)]),
                        )
                        count += 1
                        for k in range(0, 4):
                            output_matrix[i + k, j + k] = input_matrix[i + k, j + k]

                if j >= 3 and i >= 3:
                    # Diagonal backwards
                    if (
                        np.array([input_matrix[i - k, j - k] for k in range(1, 4)])
                        == ["M", "A", "S"]
                    ).all():
                        print(
                            "Diagonal bottom right to top left",
                            np.array([input_matrix[i - k, j - k] for k in range(1, 4)]),
                        )
                        count += 1
                        for k in range(0, 4):
                            output_matrix[i - k, j - k] = input_matrix[i - k, j - k]

                if j < w - 3 and i >= 3:
                    # Diagonal forwards
                    if (
                        np.array([input_matrix[i - k, j + k] for k in range(1, 4)])
                        == ["M", "A", "S"]
                    ).all():
                        print(
                            "Diagonal bottom left to top right",
                            np.array([input_matrix[i - k, j + k] for k in range(1, 4)]),
                        )
                        count += 1
                        for k in range(0, 4):
                            output_matrix[i - k, j + k] = input_matrix[i - k, j + k]
                if j >= 3 and i < h - 3:
                    # Diagonal backwards
                    if (
                        np.array([input_matrix[i + k, j - k] for k in range(1, 4)])
                        == ["M", "A", "S"]
                    ).all():
                        print(
                            "Diagonal top right to bottom left",
                            np.array([input_matrix[i + k, j - k] for k in range(1, 4)]),
                        )
                        count += 1
                        for k in range(0, 4):
                            output_matrix[i + k, j - k] = input_matrix[i + k, j - k]
    print(output_matrix)
    print(count)
