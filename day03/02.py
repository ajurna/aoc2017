def get_position_in_spiral(target):
    # Identifying which 'layer' or 'ring' the target number will reside on
    layer = 0
    while (2*layer+1)**2 < target:
        layer += 1

    # The length of an edge of this layer
    edge_length = 2*layer+1

    # The maximum number within this layer
    max_num = edge_length**2

    # Distance of target from the max number
    dist = max_num - target

    # Identifying quadrant:
    # This will be a number between 0 and 3, inclusive
    quadrant = dist // (edge_length-1)

    # Position within quadrant
    position = dist % (edge_length-1)

    # Now we will calculate the coordinates (x, y)
    if quadrant == 0:
        x = layer
        y = -position
    elif quadrant == 1:
        x = -position
        y = layer
    elif quadrant == 2:
        x = -layer
        y = position
    else:  # quadrant == 3
        x = position
        y = -layer

    # Adjust coordinates for 'zero-indexed' 2D array (matrix)
    x += n // 2
    y = n // 2 - y  # Flip y due to array's top-down nature

    return (x, y)

n = 5
target = 17
x, y = get_position_in_spiral(265149)
print(f"The number {target} is located at position ({x}, {y}) in a {n}x{n} spiral.")

def get_layer(n):
    layer = 0
    while (2 * layer + 1) ** 2 < n:
        layer += 1
    return layer

n = 265149
d = get_layer(n)  # the Manhattan distance from the center
print(f"The Manhattan distance from number {n} to the center is {d}.")