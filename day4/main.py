def parse_data():
    grid = []
    with open("input.txt", "r") as file:
        for line in file:
            row = list(line.strip())
            grid.append(row)
    return grid

def check_char(char, index):
    return char == "XMAS"[index]

def check_word_xmas(grid, y_coord, x_coord, direction):
    for index in range(4):
        # check boundaries and set char to check
        try:
            char = ""
            match direction:
                case "right":
                    if direction == "right" and x_coord + index < 0: return False 
                    char = grid[y_coord][x_coord+index]
                case "left":
                    if direction == "left" and x_coord - index < 0: return False
                    char = grid[y_coord][x_coord-index]
                case "down":
                    if direction == "left" and x_coord + index < 0: return False
                    char = grid[y_coord+index][x_coord]
                case "up":
                    if direction == "up" and y_coord - index < 0: return False
                    char = grid[y_coord-index][x_coord]
                case "down right":
                    if direction == "down right" and (y_coord + index < 0) or (x_coord + index < 0):
                        return False
                    char = grid[y_coord+index][x_coord+index]
                case "down left":
                    if direction == "down left" and ((y_coord + index) < 0 or (x_coord - index < 0)):
                        return False
                    char = grid[y_coord+index][x_coord-index]
                case "up right":
                    if direction == "up right" and ((y_coord - index) < 0 or (x_coord + index < 0)):
                        return False
                    char = grid[y_coord-index][x_coord+index]
                case "up left":
                    if direction == "up left" and ((y_coord - index) < 0 or (x_coord - index < 0)):
                        return False
                    char = grid[y_coord-index][x_coord-index]
        except:
            return False

        # check char is correct place
        if not check_char(char, index):
            return False

    # if all conditions met should spell xmas
    return True

def check_cross_mas(grid, y_coord, x_coord):
    return False

 
def traverse_grid(grid):
    total_p1 = 0
    total_p2 = 0
    directions = ["right", "left", "down", "up", "down right", "down left", "up right", "up left"]
    for y_coord, row in enumerate(grid):
        for x_coord, char in enumerate(row):
            # part one    
            if char == "X":
                for direction in directions:
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
