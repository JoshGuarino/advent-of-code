def parse_input():
    grid = [] 
    with open("input.txt", "r") as file:
        for line in file:
            grid.append(list(line))

def main():
    grid = parse_input()

if __name__ == "__main__":
    main()
