import constant
import minimax
import copy

def cpu_turn(state, canvas):
    temp_state = copy.deepcopy(state)
    val_list = [-1000]*constant.grid
    for i in range(constant.grid):
        temp = copy.deepcopy(temp_state)
        temp_new = constant.successor(temp, i, 'p')
        if temp_new == None:
            continue
        val_list[i] = minimax.minimax(temp_new, constant.depth - 1, False)
    pos = val_list.index(max(val_list))
    print(val_list, pos)
    # maxi = 0
    # pos = 0
    # for i in range(constant.grid):
    #     if state[0][i] == None:
    #         if val_list[i]>=maxi:
    #             pos = i
    #             maxi = val_list[i]
    constant.state_change(pos, state, canvas, 'p')
