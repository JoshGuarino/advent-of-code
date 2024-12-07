import itertools

def parse_input():
    equations = dict()
    with open("input.txt", "r") as file:
        for line in file:
            split_line = line.split(":")
            test_value = int(split_line[0])
            nums = split_line[1].split()
            equations[test_value] = [int(num) for num in nums] 
    return equations

def evaluate_expression(test_value, nums):
    operator_positions = len(nums) - 1
    for operators in itertools.product("+*", repeat=operator_positions):
        result = nums[0]
        for index, op in enumerate (operators):
            if op == "+":
                result += nums[index + 1]
            elif op == "*":
                result *= nums[index + 1]
        if result == test_value:
            return True
    return False

def find_total_calibration(equations):
    total_calibration = 0
    for test_value, nums in equations.items():
        if evaluate_expression(test_value, nums):
            total_calibration += test_value
    return total_calibration

def main():
    equations = parse_input()
    total_calibration = find_total_calibration(equations)
    print(total_calibration)

if __name__ == "__main__":
    main()
