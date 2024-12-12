def parse_input() -> list[str]:
    with open("input.txt", "r") as file:
        grid = []
        for line in file:
            grid.append(list(line)[:-1])
    return grid

def get_neighbors(x_coord: int, y_coord: int, rows: int, cols: int):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dir_x, dir_y in directions:
        neighbor_x, neighbor_y = x_coord + dir_x, y_coord + dir_y
        if 0 <= neighbor_x < rows and 0 <= neighbor_y < cols:
            yield neighbor_x, neighbor_y

def calculate_area_and_perimeter(garden_map: list[str], x_coord: int, y_coord: int, plant_type: str, visited: set) -> tuple:
    area = 0
    perimeter = 0

    return area, perimeter

def calculate_total_price(garden_map: list[str]) -> int:
    visited = set()
    total_price = 0
    for x_index, row in enumerate(garden_map):
        for y_index, plant_type in enumerate(row): 
            if (x_index, y_index) not in visited:
                area, perimeter = calculate_area_and_perimeter(garden_map, x_index, y_index, plant_type, visited)
                total_price += area * perimeter
    return total_price

def main():
    garden_map = parse_input()
    total_price = calculate_total_price(garden_map)
    print(total_price)

if __name__ == "__main__":
    main()
