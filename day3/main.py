import re

# regex patterns for various instructions
mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

def calculate_sum(memory):
    # find all mul instructions and calc the sum
    matches = re.findall(mul_pattern, memory)
    total = sum(int(x) * int(y) for x, y in matches)
    return total

def calculate_sum_conditions(memory):
    is_enabled = True 
    total = 0

    # tokenize the memory into individual instructions
    tokens = re.split(r"(mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\)|do\(\)|don't\(\))", memory)
    for token in tokens:
        token = token.strip() # strip whitepspace
        if not token: # skip empty tokens
            continue 
        
        # conditionals to match instructions
        if re.match(do_pattern, token):
            is_enabled = True
        elif re.match(dont_pattern, token):
            is_enabled = False
        elif match := re.match(mul_pattern, token):
            if is_enabled:
                x, y = map(int, match.groups())
                total += x * y
    return total

def main():
    with open("input.txt", "r") as file:
        memory = file.read()
    total_p1 = calculate_sum(memory)
    total_p2 = calculate_sum_conditions(memory)
    print(total_p1)
    print(total_p2)

if __name__ == "__main__":
    main()
