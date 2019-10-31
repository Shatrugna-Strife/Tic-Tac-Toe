import constant
import copy

def minimax(state, depth, max_player):
    temp_heu = constant.heuristic(state)
    if depth == 0 or temp_heu == 100 or temp_heu == -100:
        # print("yes")
        return temp_heu

    if max_player:
        # temp_pos = None
        max_eval = -1000
        for i in range(constant.grid):
            temp_state = copy.deepcopy(state)
            temp = constant.successor(temp_state, i, 'p')
            # print(state, temp, i)
            if temp == None:
                continue
            else:
                eval = minimax(temp, depth-1, False)
            max_eval = max(max_eval, eval)
        #     if max_eval == eval and depth == constant.depth:
        #         temp_pos = i
        # if depth == constant.depth:
        #     # print(1)
        #     return temp_pos
        return max_eval
    else:
        # temp_pos = None
        min_eval = 1000
        for i in range(constant.grid):
            temp_state = copy.deepcopy(state)
            temp = constant.successor(temp_state, i, 'u')
            if temp == None:
                continue
            else:
                eval = minimax(temp, depth-1, True)
            min_eval = min(min_eval, eval)
        #     if min_eval == eval and depth == constant.depth:
        #         temp_pos = i
        #
        # if depth == constant.depth:
        #     return temp_pos
        return min_eval
#Use alpha = -1000 and beta = 1000
def minimax_alpha_beta(state, depth, alpha, beta, max_player):
    temp_heu = constant.heuristic(state)

    if depth == 0 or temp_heu == 100 or temp_heu == -100:
        return temp_heu

    if max_player:
        # temp_pos = None
        max_eval = -1000
        for i in range(constant.grid):
            temp_state = copy.deepcopy(state)
            temp = constant.successor(temp_state, i, 'p')
            # print(state, temp)
            if temp == None:
                continue
            else:
                eval = minimax_alpha_beta(temp, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            # if max_eval == eval and depth == constant.depth:
            #     temp_pos = i
                # print(temp_pos)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        # if depth == constant.depth:
        #     # print(depth)
        #     return temp_pos
        return max_eval
    else:
        temp_pos = None
        min_eval = 1000
        for i in range(constant.grid):
            temp_state = copy.deepcopy(state)
            temp = constant.successor(temp_state, i,'u')
            if temp == None:
                continue
            else:
                eval = minimax_alpha_beta(temp, depth-1, alpha, beta, False)
            min_eval = min(min_eval, eval)
            # if min_eval == eval and depth == constant.depth:
            #     temp_pos = i
            beta = min(beta, eval)
            if beta <= alpha:
                break
        # if depth == constant.depth:
        #     # print(depth)
        #     return temp_pos
        return min_eval
