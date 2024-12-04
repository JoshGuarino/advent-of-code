WORD = "XMAS"

def parse_data():
    grid = []
    with open("input.txt", "r") as file:
        for line in file:
            row = list(line.strip())
            grid.append(row)
    return grid

def check_char(char, index):
    return char == WORD[index]

def in_boundary(index, y_coord, x_coord, direction):
    # Check boundaries based on direction
    if direction == "right" and x_coord + index < 0: 
        return False
    elif direction == "left" and x_coord - index < 0:
        return False
    elif direction == "down" and y_coord + index < 0:
        return False
    elif direction == "up" and y_coord - index < 0:
        return False
    elif direction == "down right" and ((y_coord + index < 0) or (x_coord + index < 0)):
        return False
    elif direction == "down left" and ((y_coord + index) < 0 or (x_coord - index < 0)):
        return False
    elif direction == "up right" and ((y_coord - index) < 0 or (x_coord + index < 0)):
        return False
    elif direction == "up left" and ((y_coord - index) < 0 or (x_coord - index < 0)):
        return False
    return True

def check_word(grid, y_coord, x_coord, direction):
    for index in range(4):
        # out of bounds check cause of negative indexes in python
        if not in_boundary(index, y_coord, x_coord, direction): 
            return False
        try:
            char = ""
            match direction:
                case "right":
                    char = grid[y_coord][x_coord+index]
                case "left":
                    char = grid[y_coord][x_coord-index]
                case "down":
                    char = grid[y_coord+index][x_coord]
                case "up":
                    char = grid[y_coord-index][x_coord]
                case "down right":
                    char = grid[y_coord+index][x_coord+index]
                case "down left":
                    char = grid[y_coord+index][x_coord-index]
                case "up right":
                    char = grid[y_coord-index][x_coord+index]
                case "up left":
                    char = grid[y_coord-index][x_coord-index]
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
