from collections import defaultdict

def parse_input() -> dict[str, int]:
    with open("input.txt", "r") as file:
        stones = defaultdict(int)
        for stone in file.read().split():
            stones[stone] = 1
        return stones

def simulate_blinks(stones: dict[str, int], blinks: int):
    for _ in range(blinks):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            if stone == "0":
                new_stones["1"] += count
            elif len(stone) % 2 == 0:
                new_stones[str(int(stone[:len(stone)//2]))] += count
                new_stones[str(int(stone[len(stone)//2:]))] += count
            else:
                new_stones[str(int(stone) * 2024)] += count
        stones = new_stones
    return sum(stones.values())

def main() -> None:
    # part one
    stones_p1 = parse_input() 
    t_stones_p1_count = simulate_blinks(stones_p1, 25)
    print(t_stones_p1_count)
    
    # part two
    stones_p2 = parse_input()
    t_stones_p2_count = simulate_blinks(stones_p2, 75)
    print(t_stones_p2_count)

if __name__ == "__main__":
    main()
