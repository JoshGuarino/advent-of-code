def parse_data():
    grid = []
    with open("input.txt", "r") as file:
        for line in file:
            row = list(line.strip())
            grid.append(row)
    return grid

def check_word_xmas(grid, y_coord, x_coord, direction):
    XMAS = "XMAS"
    for index in range(4):
        # define boundary checks 
        EXCEEDS_RIGHT_BOUND = x_coord + index < 0
        EXCEEDS_LEFT_BOUND = x_coord - index < 0 
        EXCEEDS_DOWN_BOUND = y_coord + index < 0
        EXCEEDS_UP_BOUND = y_coord - index < 0

        # check boundaries and set char if possible        
        try:
            char = ""
            match direction:
                case "right":
                    if EXCEEDS_RIGHT_BOUND: return False 
                    char = grid[y_coord][x_coord+index]
                case "left":
                    if EXCEEDS_LEFT_BOUND: return False
                    char = grid[y_coord][x_coord-index]
                case "down":
                    if EXCEEDS_DOWN_BOUND: return False
                    char = grid[y_coord+index][x_coord]
                case "up":
                    if EXCEEDS_UP_BOUND: return False
                    char = grid[y_coord-index][x_coord]
                case "down right":
                    if EXCEEDS_DOWN_BOUND or EXCEEDS_RIGHT_BOUND: return False
                    char = grid[y_coord+index][x_coord+index]
                case "down left":
                    if EXCEEDS_DOWN_BOUND or EXCEEDS_LEFT_BOUND: return False  
                    char = grid[y_coord+index][x_coord-index]
                case "up right":
                    if EXCEEDS_UP_BOUND or EXCEEDS_RIGHT_BOUND: return False
                    char = grid[y_coord-index][x_coord+index]
                case "up left":
                    if EXCEEDS_UP_BOUND or EXCEEDS_LEFT_BOUND: return False
                    char = grid[y_coord-index][x_coord-index]
        except:
            return False

        # check char is correct place
        if not char == XMAS[index]:
            return False

    # if all conditions met word should spell xmas
    return True



def check_cross_mas(grid, y_coord, x_coord):
    # define the "MAS" pattern
    MAS = ["M", "A", "S"]
    MAS_REV = ["S", "A", "M"]

    # ensure bounds for a 3x3 region centered at (y, x)
    TOP_ROW_BOUND = y_coord - 1 >= 0
    BOT_ROW_BOUND = y_coord + 1 < len(grid)
    LEFT_COL_BOUND = x_coord - 1 >= 0
    RIGHT_COL_BOUND = x_coord + 1 < len(grid[0])
    if not all([TOP_ROW_BOUND, BOT_ROW_BOUND, LEFT_COL_BOUND, RIGHT_COL_BOUND]):
        return False

    # Extract diagonals
    down_right = [
        grid[y_coord - 1][x_coord - 1],
        grid[y_coord][x_coord],
        grid[y_coord + 1][x_coord + 1]
    ]
    up_right = [
        grid[y_coord + 1][x_coord - 1],
        grid[y_coord][x_coord],
        grid[y_coord - 1][x_coord + 1]
    ]

    # Check if either diagonal matches "MAS" or its reverse
    diagonal_1_matches = down_right == MAS or down_right == MAS_REV 
    diagonal_2_matches = up_right == MAS or up_right == MAS_REV 
    return diagonal_1_matches and diagonal_2_matches
 
def traverse_grid(grid):
    total_p1 = 0
    total_p2 = 0
    DIRECTIONS = ["right", "left", "down", "up", "down right", "down left", "up right", "up left"]
    for y_coord, row in enumerate(grid):
        for x_coord, char in enumerate(row):
            # part one    
            if char == "X":
                for direction in DIRECTIONS:
                    total_p1 += 1 if check_word_xmas(grid, y_coord, x_coord, direction) else 0

            # part two
            if check_cross_mas(grid, y_coord, x_coord):
                total_p2 += 1 

    return [total_p1, total_p2]

def main():
    grid = parse_data()
    total_p1, total_p2 = traverse_grid(grid)
    print(total_p1)
    print(total_p2)

if __name__ == "__main__":
    main()
