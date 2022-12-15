def generate_unit_of_sand(grid, offset):
    sand_idx = [0, 500 - offset]

    for row in range(1, len(grid)):
        if grid[row][sand_idx[1]] == '.':
            sand_idx = [row, sand_idx[1]]
        elif grid[row][sand_idx[1] - 1] == '.':
            sand_idx = [row, sand_idx[1] - 1]
        elif grid[row][sand_idx[1] + 1] == '.':
            sand_idx = [row, sand_idx[1] + 1]
        else:
            break

    grid[sand_idx[0]][sand_idx[1]] = 'o'


def source_blocked(grid, offset):
    if grid[0][500 - offset] == 'o':
        return True
    else:
        return False


def draw_line(first_vertex, second_vertex, grid, offset):
    if first_vertex[1] == second_vertex[1]:
        smaller = min(first_vertex[0], second_vertex[0])
        bigger = max(first_vertex[0], second_vertex[0])
        for col in range(smaller, bigger + 1):
            grid[first_vertex[1]][col - offset] = '#'
    else:
        smaller = min(first_vertex[1], second_vertex[1])
        bigger = max(first_vertex[1], second_vertex[1])
        for row in range(smaller, bigger + 1):
            grid[row][first_vertex[0] - offset] = '#'


def process_input():
    with open('inputs/puzzle_1.txt') as f:
        lines = f.readlines()

    min_col = 1000
    max_col = 0
    max_row = 0
    for line in lines:
        line = line.replace('\n', '')
        vertices = line.split(" -> ")

        for vertex in vertices:
            components = vertex.split(",")
            min_col = min(min_col, int(components[0]))
            max_col = max(max_col, int(components[0]))
            max_row = max(max_row, int(components[1]))

    min_col -= 500
    max_col += 500

    offset = min_col - 1

    grid = [['.' for i in range(min_col - 1, max_col + 2)] for j in range(0, max_row + 3)]
    grid[len(grid) - 1] = ['#' for i in range(min_col - 1, max_col + 2)]

    grid[0][500 - offset] = '+'

    for line in lines:
        line = line.replace('\n', '')
        vertices = line.split(" -> ")

        curr_vertex_components = vertices[0].split(",")
        for vertex_idx in range(1, len(vertices)):
            next_vertex_components = vertices[vertex_idx].split(",")
            draw_line([int(component) for component in curr_vertex_components],
                      [int(component) for component in next_vertex_components], grid, offset)
            curr_vertex_components = next_vertex_components

    units_of_sand = 0
    while not source_blocked(grid, offset):
        generate_unit_of_sand(grid, offset)
        units_of_sand += 1

    for row in grid:
        print(row)

    print(units_of_sand)


if __name__ == "__main__":
    process_input()
