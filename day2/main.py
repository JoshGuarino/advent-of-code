def parse_data():
    data = []
    with open("input.txt", "r") as file:
        for line in file:
            report = [int(num) for num in line.split()]
            data.append(report)  
    return data

def check_safety(report):
    increasing = False
    decreasing = False
    for index, num in enumerate(report):
        # if we make it to end its a good report
        if num == report[-1]:
            return True

        # get the difference bewtween current and next num
        diff = num - report[index+1]

        # check for out of bounds diffrence
        if diff == 0 or diff > 3 or diff < -3:
            return False

        # set flags for decreasing or increasing
        if diff > 0:
            increasing = True
        elif diff < 0:
            decreasing = True
        else:
            return False
       
        # both being true idicates a change in dirtection
        if decreasing and increasing:
            return False
        



def main():
    data = parse_data()   
    safe_reports = 0
    for index, report in enumerate(data):
        if check_safety(report):
            safe_reports += 1
    print(safe_reports)

if __name__ == "__main__":
    main()
