def cells(cell_numbers):
    x = cell_numbers
    value = "♘"
    g1 = "┏"
    gx = " ━ ┓"
    top = " ━ ┳"
    line_1 = g1 + top * (x-1) + gx
    print(line_1)
    pipe = "┃"
    line_2 = f"{pipe}" + f" {value} {pipe}" * x
    print(line_2)
    g3 = "┗"
    gx3 = " ━ ┛"
    middle3 = " ━ ┻"
    line_3 = g3 + middle3 * (x-1) + gx3
    print(line_3)

cells(5)
cells(5)
cells(5)



def matrix(n, picture=" "):

    left_corner = "┏"
    right_top_corner = " ━ ┓"
    middle_top = " ━ ┳"

    left_bottom_corner = "┗"
    right_bottoom_corner = " ━ ┛"
    middle_bottom = " ━ ┻"

    top_line = left_corner + middle_top * (n-1) + right_top_corner
    bottom_line = \
        left_bottom_corner + middle_bottom * (n-1) + right_bottoom_corner
    pipe = "┃"
    value = picture
    pipes = pipe + f" {value} {pipe}" * n

    cross = " ━ ╋"
    right_pin = " ━ ┫"
    left_pin = "┣"
    inter_cells = left_pin + cross * (n-1) + right_pin

    print(top_line, pipes, sep="\n")
    for i in range(n):
        print(inter_cells, pipes, sep="\n")
    print(bottom_line)




matrix(10)