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

def find_last_used_block_index(disk_map: list[str], stop_index) -> int | None:
        for index, blocks in reversed(list(enumerate(disk_map))):
            if index == stop_index:
                return
            if blocks == ".":
                continue
            return index

def compact_disk_map(decomp_disk_map: list[str]) -> list[str]:
    disk_map = decomp_disk_map
    for index, block in enumerate(disk_map):
        if block != ".":
            continue
        block_index = find_last_used_block_index(disk_map, index)
        if not block_index:
            break
        disk_map[index] = disk_map[block_index]
        disk_map[block_index] = "."

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
    decomp_disk_map = decompresss_disk_map(disk_map)
    comp_disk_map = compact_disk_map(decomp_disk_map)
    check_sum = find_check_sum(comp_disk_map)
    print(check_sum)

if __name__ == "__main__":
    main()
