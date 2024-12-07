def parse_input():
    equations = dict()
    with open("input.txt", "r") as file:
        for line in file:
            split_line = line.split(":")
            test_value = int(split_line[0])
            nums = split_line[1].split()
            equations[test_value] = [int(num) for num in nums] 
    return equations

def evaluate_expression():
    pass

def find_total_calibaration(equations):
    total_calibaration = 0
    for test_value, nums in equations.items():
        for num in nums:
            pass

def main():
    equations = parse_input()
    find_total_calibaration(equations)

if __name__ == "__main__":
    main()
