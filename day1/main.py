def main():
    total_dist = 0
    left_list = []
    right_list = []

    with open("input.txt", "r") as file:
        for line in file:            
            nums = line.split()
            left_list.append(int(nums[0]))
            right_list.append(int(nums[1]))
            
    left_list.sort()
    right_list.sort()

    for index, num in enumerate(left_list):
        diff = num - right_list[index]
        total_dist += abs(diff) 

    print(total_dist)

if __name__ == "__main__":
    main()
