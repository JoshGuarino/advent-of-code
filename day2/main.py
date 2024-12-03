def parse_data():
    data = []
    with open("input.txt", "r") as file:
        for line in file:
            report = [int(num) for num in line.split()]
            data.append(report)  
    return data

# check safety under original rules
def check_safety(report):
    # flags for checking change is direction 
    increasing = False
    decreasing = False

    # loop through until second to last iteration
    for index, num in enumerate(report[:-1]):
        # calculate difference between current and next num
        diff = num - report[index+1]

        # out of bounds check
        if diff == 0 or abs(diff) > 3:
            return False

        # set if current iteration is increasing or decreasing
        if diff > 0:
            increasing = True
        elif diff < 0:
            decreasing = True

        # if both flags are true it indicates a change in direction
        if decreasing and increasing:
            return False

    # if we make it through all iterations its safe
    return True

# check safety if 1 bad level removed
def check_safety_minus_one(report):
    # check if report safe without modification 
    if check_safety(report):
        return True

    # check if safe when excluding current level
    for index, _ in enumerate(report):
        modified_report = report[:index] + report[index + 1:]
        if check_safety(modified_report):
            return True

   # if we make it thorugh all iterations its unsafe 
    return False

def main():
    data = parse_data()   
    safe_reports_p1 = 0
    safe_reports_p2 = 0

    for report in data:
        # part one
        if check_safety(report):
            safe_reports_p1 += 1
        
        # part two
        if check_safety_minus_one(report):
            safe_reports_p2 += 1

    print(safe_reports_p1)
    print(safe_reports_p2) 

if __name__ == "__main__":
    main()
