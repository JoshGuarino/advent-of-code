def parse_data():
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")
        separator_index = lines.index('')  # Find the blank line separating the two sections
        rule_lines = lines[:separator_index]
        update_lines = lines[separator_index + 1:]

        # Parse rules
        rules = []
        for line in rule_lines:
            x, y = map(int, line.split("|"))
            rules.append((x, y))

        # Parse updates
        updates = []
        for line in update_lines:
            udpate = list(map(int, line.split(",")))
            updates.append(udpate)

    return rules, updates

def is_correctly_ordered(update, rules):
    # Check if the update is in the correct order according to the rules
    page_position = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in page_position and y in page_position:
            if page_position[x] > page_position[y]:
                return False
    return True

def main():
    rules, updates = parse_data()
    middle_sum = 0
    for update in updates:
        if is_correctly_ordered(update, rules):
            middle_page = update[len(update) // 2]
            middle_sum += middle_page
    print(middle_sum)

if __name__ == "__main__":
    main()
