def parse_input() -> str:
    with open("input.txt", "r") as file:
        return file.read().strip()

def decompresss_disk_map(disk_map: str) -> list[str]:
    decomp_disk_map = []
    is_free_space = False
    current_id = 0
    for blocks in disk_map:
        num_blocks = int(blocks)
        for _ in range(num_blocks):
            if not is_free_space:
                decomp_disk_map.append(str(current_id))
            else:
                decomp_disk_map.append(".")
        if not is_free_space:
            current_id += 1
        is_free_space = False if is_free_space else True

    return decomp_disk_map

def find_last_used_block_index(disk_map: list[str]) -> int:
    for index in range(len(disk_map) - 1, -1, -1):
        if disk_map[index] != ".":
            return index
    return -1

def compact_disk_map(disk_map: list[str]) -> list[str]:
    tail = find_last_used_block_index(disk_map)
    if tail < 0:
        return disk_map
    for index, block in enumerate(disk_map):
        if tail <= index:
            break
        if block != ".":
            continue
        disk_map[index] = disk_map[tail]
        disk_map[tail] = "."
        tail = find_last_used_block_index(disk_map[:tail])

    return disk_map 

def comp_disk_map_by_blocks(disk_map: list[str]) -> list[str]:
    return disk_map

def find_check_sum(disk_map: list[str]) -> int:
    check_sum = 0
    for index, block in enumerate(disk_map):
        if block == ".":
            continue
        check_sum += (index * int(block))
    return check_sum

def main() -> None:
    disk_map = parse_input()
    disk_map = "12345"
    
    # part one
    decomp_disk_map = decompresss_disk_map(disk_map)
    comp_disk_map = compact_disk_map(decomp_disk_map)
    check_sum_p1 = find_check_sum(comp_disk_map)
    print(check_sum_p1)
    
    # part two
    decomp_disk_map = decompresss_disk_map(disk_map)
    comp_disk_map = comp_disk_map_by_blocks(decomp_disk_map)
    check_sum_p2 = find_check_sum(comp_disk_map)
    print(check_sum_p2)

if __name__ == "__main__":
    main()
