def parse_input():
    with open("input.txt", "r") as file:
        grid = []
        for line in file:
            grid.append(list(line)[:-1])
    return grid

def get_neighbors():
    pass

def calculate_area_and_perimeter():
    pass

def calculate_total_price():
    pass

def main():
    grid = parse_input()
    print(grid)

if __name__ == "__main__":
    main()
