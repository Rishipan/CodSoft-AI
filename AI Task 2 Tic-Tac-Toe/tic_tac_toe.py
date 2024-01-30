import math

# constants
Ai = 'O'
Human = 'X'
blank = '-'
# blank = ['0','1','2','3','4','5','6','7','8']

def print_board(board):
        for row in [board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

# check winner
def check_winner(board, player):
    win_combi = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combi in win_combi:
        if all(board[i] == player for i in combi):
            return True
    return False

# check board if full!
def is_board_full(board):
    return all(cell != blank for cell in board)


# minmax algorithm
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    
    if check_winner(board, Ai):
        return 1
    elif check_winner(board, Human):
        return -1
    elif is_board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == blank:
                board[i] = Ai
                eval_score = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = blank
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == blank:
                board[i] = Human
                eval_score = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = blank
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
        return min_eval

# best move
def find_best_move(board):
    best_move = -1
    best_eval = -math.inf
    for i in range(9):
        if board[i] == blank:
            board[i] = Ai
            eval_score = minimax_alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = blank
            if eval_score > best_eval:
                best_eval = eval_score
                best_move = i
    return best_move

def play_game():
    board1 = [str(i) for i in range(9)]
    board2 = [blank] * 9
    while True:
        print("\nInitial Board:")
        print_board(board1)
        print()
        print("Current Board:")
        print_board(board2)
        move = int(input("Select your move (0-8): "))
        
        if board2[move] == blank:
            board2[move] = Human
            
            if check_winner(board2, Human):
                print_board(board2)
                print("Human win!")
                break
            elif is_board_full(board2):
                print_board(board2)
                print("It's a draw!")
                break
            
            ai_move = find_best_move(board2)
            board2[ai_move] = Ai
            
            if check_winner(board2, Ai):
                print_board(board2)
                print("AI wins!")
                break
            elif is_board_full(board2):
                print_board(board2)
                print("It's a draw!")
                break
        else:
            print("It's already filled! Try again.")

if __name__ == "__main__":
    play_game()

