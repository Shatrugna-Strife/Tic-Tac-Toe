rect_diff = 10
start = 50
grid_size = 50
grid = 4
depth = 8

def state_change(y, state, main_canvas, player):
    x = 0
    print(y)
    for i in range(grid-1, -1, -1):
        if state[i][y] == None:
            x = i
            break
    color = None
    if player == 'u':
        color = 'green'
        state[x][y] = 'u'
    else:
        color = 'red'
        state[x][y] = 'p'
    main_canvas.create_oval(start+y*grid_size, start+x*grid_size, start+(y+1)*grid_size, start+(x+1)*grid_size, fill = color)

def successor(state, pos, turn):
    x = None
    for i in range(grid-1, -1, -1):
        if state[i][pos] == None:
            x = i
            break
    if x == None:
        return None
    else:
        state[x][pos] = turn
    return state

def heuristic(state):
    score = 0
    center_x = grid - 2
    center_y = grid - 2
    for i in range(1, center_y+1):
        for j in range(1, center_x+1):
            for k in range(3):
                if state[i+k-1][j-1] == state[i+k-1][j] and state[i+k-1][j] == state[i+k-1][j+1]:
                    if state[i+k-1][j-1] == 'p':
                        return 100
                    elif state[i+k-1][j-1] == 'u':
                        return -100
            for k in range(3):
                if state[i-1][j+k-1] == state[i][j+k-1] and state[i+1][j+k-1] == state[i][j+k-1]:
                    if state[i-1][j+k-1] == 'p':
                        return 100
                    elif state[i-1][j+k-1] == 'u':
                        return -100

            if state[i-1][j-1] == state[i][j] and state[i][j] == state[i+1][j+1]:
                if state[i-1][j-1] == 'p':
                    return 100
                elif state[i-1][j-1] == 'u':
                    return -100
            if state[i+1][j-1] == state[i][j] and state[i][j] == state[i-1][j+1]:
                if state[i+1][j-1] == 'p':
                    return 100
                elif state[i+1][j-1] == 'u':
                    return -100
    return score
