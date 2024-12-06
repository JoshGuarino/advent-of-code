def parse_input():
    grid = [] 
    guard_pos = tuple()
    guard_dir = ""
    with open("input.txt", "r") as file:
        for row_index, col in enumerate(file):
            row = list(col) 
            grid.append(row)
            for col_index, pos in enumerate(row):
                if pos == "^" or pos == ">" or pos == "v" or pos == "<":
                    guard_pos = (row_index, col_index)
                    guard_dir = pos
    return grid, guard_pos, guard_dir 

def sim_guard_path(grid, guard_pos, guard_dir):
    dirs = ['^', '>', 'v', '<']
    dir_deltas = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    visited_pos = set()
    visited_pos.add(guard_pos)
    rows = len(grid)
    cols = len(grid[0])

    while True:
        # Calculate the position directly in front of the guard
        row, col = dir_deltas[guard_dir]
        next_pos = (guard_pos[0] + row, guard_pos[1] + col)
        
        # Check if the next position is within bounds
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        # Check if the next position is an obstacle
        if grid[next_pos[0]][next_pos[1]] == '#':
            # Turn right (cycle to the next direction)
            guard_dir = dirs[(dirs.index(guard_dir) + 1) % 4]
            continue
        
        # Move forward
        guard_pos = next_pos
        visited_pos.add(guard_pos)
    
    return len(visited_pos)

def main():
    grid, guard_pos, guard_dir = parse_input()
    distinct_pos = sim_guard_path(grid, guard_pos, guard_dir)
    print(distinct_pos)

if __name__ == "__main__":
    main()
