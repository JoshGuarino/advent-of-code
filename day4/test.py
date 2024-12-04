def parse_data():
    grid = []
    with open("input.txt", "r") as file:
        for line in file:
            row = list(line.strip())
            grid.append(row)
    return grid

def check_char(char, index):
    # Check if the character at index matches the corresponding character
    if index == 0:
        return char == "X"
    elif index == 1:
        return char == "M"
    elif index == 2:
        return char == "A"
    elif index == 3:
        return char == "S"

def check_word(grid, y_coord, x_coord, direction):
    # Check if the word "XMAS" exists in the given direction
    for index in range(4):
        char = ""
        try:
            # Determine the character based on the direction
            match direction:
                case "right":
                    if x_coord + index >= len(grid[0]): return False
                    char = grid[y_coord][x_coord + index]
                case "left":
                    if x_coord - index < 0: return False
                    char = grid[y_coord][x_coord - index]
                case "down":
                    if y_coord + index >= len(grid): return False
                    char = grid[y_coord + index][x_coord]
                case "up":
                    if y_coord - index < 0: return False
                    char = grid[y_coord - index][x_coord]
                case "down right":
                    if y_coord + index >= len(grid) or x_coord + index >= len(grid[0]): return False
                    char = grid[y_coord + index][x_coord + index]
                case "down left":
                    if y_coord + index >= len(grid) or x_coord - index < 0: return False
                    char = grid[y_coord + index][x_coord - index]
                case "up right":
                    if y_coord - index < 0 or x_coord + index >= len(grid[0]): return False
                    char = grid[y_coord - index][x_coord + index]
                case "up left":
                    if y_coord - index < 0 or x_coord - index < 0: return False
                    char = grid[y_coord - index][x_coord - index]
        except:
            return False
        if not check_char(char, index):
            return False
    return True

def traverse_grid(grid):
    total = 0
    directions = [
        "right", "left", "down", "up", "down right", "down left", "up right", "up left"
    ]
    for y_coord, row in enumerate(grid):
        for x_coord, char in enumerate(row):
            if char == "X":
                for direction in directions:
                    total += 1 if check_word(grid, y_coord, x_coord, direction) else 0
    return total

def main():
    grid = parse_data()
    total = traverse_grid(grid)
    print(total)

if __name__ == "__main__":
    main()

