import re

def calculate_sum(memory):
    pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    matches = re.findall(pattern, memory)
    total = sum(int(x) * int(y) for x, y in matches)
    return total

def main():
    with open("input.txt", "r") as file:
        memory = file.read()

    # part one
    result = calculate_sum(memory)
    print(result)

if __name__ == "__main__":
    main()
