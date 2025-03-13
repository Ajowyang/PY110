def calculate_leftover_blocks(available_blocks):
    blocks_remaining = available_blocks
    current_layer = 0
    while blocks_remaining:
        current_layer += 1
        blocks_required = current_layer * current_layer
        if blocks_remaining < blocks_required:
            return blocks_remaining
        else:
            blocks_remaining -= blocks_required
    return blocks_remaining


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
