#Creates game board of length of subjects
def board_game (trusting):
    row = len(trusting) + 1
    col = len(trusting) + 1
    print()
    board = [["." for _ in range(col)] for _ in range(row)]
    return board 

#Updates board after each question result
def update_board(board, sub_x, sub_y, result):
    if result is True:
        board_result = "Y"
    elif result is False:
        board_result = "N"
    board[sub_x - 1][sub_y -1] = board_result
    #print(board)
    return(board)

#Prints current board
def print_board(board, subjects):
    #print(board)
    print("Does subject x trust subject y?")
    for i in range(0, subjects + 1):  # Iterate over the range of subjects
        print(str(i).ljust(3), end=" " )  # Print the subject number
    print()
    count = 1
    for sublist in board:
        print(str(count).ljust(3), end= " ")
        count += 1
        for item in sublist:
            print(str(item).ljust(3), end=" ")
        print()
        
#Marks board with result of who trusts who
def sub_x_trusts_sub_y(sub_x, sub_y, trust_to_trusting):
    #print(sub_x, sub_y)
    # print(trust_to_trusting.get(sub_x), trust_to_trusting[sub_x])
    if sub_x not in trust_to_trusting:
        print ("No")
        return False
    if sub_y in trust_to_trusting[sub_x]:
        print ("Subject " + str(sub_x) + " trusts " + str(sub_y))
        if sub_x == sub_y:
            print("Only a traitor wouldn't trust thyself. Unless one was quite confused.")
        return True
    else:
        return False
    