def cacti_number(array_input):
    if not array_input:
        return 0
    
    row = len(array_input)
    col = len(array_input[0])

    def cacti(i, j):
        return (
            array_input[i][j] == 1
            and (i == 0  or array_input[i - 1][j] == 0)
            and (j == 0 or array_input[i][j - 1] == 0)
        )
    
    cacti_count = 0

    for i in range(row):
        for j in range(col):
            if cacti(i, j):
                cacti_count += 1

    return cacti_count