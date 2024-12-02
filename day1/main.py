def main():
    left_list = []
    right_list = []

    with open("input.txt", "r") as file:
        for line in file:            
            nums = line.split()
            left_list.append(int(nums[0]))
            right_list.append(int(nums[1]))
            
    left_list.sort()
    right_list.sort()

    total_dist = 0
    similar_score = 0
    for index, num in enumerate(left_list):
        # part one
        diff = num - right_list[index]
        total_dist += abs(diff) 
        
        #part two
        occurrences = right_list.count(num)
        similar_score += num*occurrences

    print(total_dist)
    print(similar_score)

if __name__ == "__main__":
    main()
