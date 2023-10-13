def cacti_number(array_input):
    if not array_input:
        return 0

    row = len(array_input)
    col = len(array_input[0])

    def can_plant_cacti(i, j):
        return (
            array_input[i][j] == 0
            and (i == 0 or array_input[i - 1][j] == 0)
            and (j == 0 or array_input[i][j - 1] == 0)
            and (i == row - 1 or array_input[i + 1][j] == 0)
            and (j == col - 1 or array_input[i][j + 1] == 0)
        )

    open_spot = 0

    for i in range(row):
        for j in range(col):
            if can_plant_cacti(i, j):
                array_input[i][j] = 1
                open_spot += 1

    return open_spot
