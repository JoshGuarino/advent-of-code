def parse_data():
    data = []
    with open("input.txt", "r") as file:
        for line in file:
            report = [int(num) for num in line.split()]
            data.append(report)  
    return data

def check_safety(report):
    # flags for checking change is direction 
    increasing = False
    decreasing = False

    # loop through until second to last iteration
    for index in range(len(report)-1):
        # calculate difference between current and next num
        diff = report[index] - report[index+1]

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

def main():
    data = parse_data()   
    safe_reports = 0
    for report in data:
        if check_safety(report):
            safe_reports += 1
    print(safe_reports)

if __name__ == "__main__":
    main()
