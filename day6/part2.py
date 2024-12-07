import numpy as np
from tqdm import tqdm
import multiprocessing

# Directions mapped to (dy, dx) for easier movement handling
DIRECTIONS = {"^": (-1, 0), "<": (0, -1), ">": (0, 1), "v": (1, 0)}


# Simulate the guard's patrol with a given map, initial position, and direction
def simulate_guard(patrol_map, start_position, start_facing, max_steps=10000):
    position = np.array(start_position)
    facing = start_facing
    visited = set()  # Track (position, facing) pairs
    steps = 0  # Step counter
    loop_detected = False

    while steps < max_steps:
        # Add current state to visited positions
        state = (tuple(position), facing)
        if state in visited:
            loop_detected = True  # Loop detected
            break  # Guard gets stuck in a loop
        visited.add(state)

        # Move in the direction the guard is facing
        dy, dx = DIRECTIONS[facing]
        new_position = position + [dy, dx]

        # Check if the new position is within bounds and not a wall
        if (
            0 <= new_position[0] < patrol_map.shape[0]
            and 0 <= new_position[1] < patrol_map.shape[1]
        ):
            if patrol_map[tuple(new_position)] == "#":
                # If there's a wall, change direction
                if facing == "^":
                    facing = ">"
                elif facing == ">":
                    facing = "v"
                elif facing == "v":
                    facing = "<"
                else:
                    facing = "^"
            else:
                # Move to the new position
                position = new_position
        else:
            # Out of bounds (guard exits the map)
            break

        steps += 1  # Increment step counter

    return loop_detected  # Return True if loop detected, False otherwise


# Function to test a single potential obstruction position
def test_obstruction(params):
    patrol_map, position, facing, i, j = params
    # Temporarily add an obstruction
    patrol_map[i, j] = "#"
    loop_detected = simulate_guard(patrol_map, position, facing)
    # Remove the obstruction
    patrol_map[i, j] = "."
    return loop_detected


# Main logic for identifying valid obstruction positions
def main():
    with open("input.txt") as f:
        patrol_map = np.array([list(l.strip()) for l in f.readlines()])
        position = None
        facing = None

        # Find the guard's starting position and facing
        for i, row in enumerate(patrol_map):
            for j, cell in enumerate(row):
                if cell in DIRECTIONS:  # Guard's starting position
                    position = (i, j)
                    facing = cell

        # Prepare the list of positions to test
        tasks = []
        for i, row in enumerate(patrol_map):
            for j, cell in enumerate(row):
                if (
                    cell == "." and (i, j) != position
                ):  # Open space, not starting position
                    tasks.append((patrol_map.copy(), position, facing, i, j))

        # Use multiprocessing to test positions in parallel with tqdm for progress tracking
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            # Create tqdm progress bar based on the number of tasks
            results = []
            with tqdm(total=len(tasks)) as pbar:
                # Using imap to update progress bar as tasks are processed
                for result in pool.imap(test_obstruction, tasks):
                    results.append(result)
                    pbar.update(1)

        # Count the number of valid positions where a loop is detected
        valid_positions = sum(results)

        print(f"Number of valid obstruction positions: {valid_positions}")


if __name__ == "__main__":
    main()
