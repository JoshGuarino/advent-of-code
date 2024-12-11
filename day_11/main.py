def parse_input() -> list[str]:
    with open("input.txt", "r") as file:
        return file.read().split() 

def count_stones(stones: list[str]):
    return len(stones)

def transform_stone(stone: str) -> list[str]:
    if stone == "0":
       return ["1"] 
    elif len(stone) % 2 == 0:
        # split even length stones
        fs = stone[:len(stone)//2].lstrip("0")
        ss = stone[len(stone)//2:].lstrip("0")
        # strip '0's from begining of stones
        second_stone = ss if ss != "" else "0"
        first_stone = fs if fs != "" else "0" 
        return [first_stone, second_stone]
    else:
        return [str(int(stone) * 2024)] 

def simulate_blinks(stones: list[str], num_blinks: int) -> list[str]:
    for _ in range(num_blinks):

        skip_iter = False
        for index, stone in enumerate(stones):
            # skip this iteration if its a newly inserted stone
            if skip_iter:
                skip_iter = False
                continue
            
            # transform the state of the stone 
            transformed_stone = transform_stone(stone)
            if len(transformed_stone) == 2:
                stones[index] = transformed_stone[0]
                stones.insert(index+1, transformed_stone[1])
                skip_iter = True
            else:
                stones[index] = transformed_stone[0]
    return stones

def main() -> None:
    stones = parse_input() 
    transformed_stones = simulate_blinks(stones, 25)
    stones_count = count_stones(transformed_stones)
    print(stones_count)
    

if __name__ == "__main__":
    main()
