import random
import PySimpleGUI as sg
import random
import questions
import game
import board
    
#subjects = game.start_game()
#traitor = game.this_is_the_traitor(game.subjects)
#trusting = game.subjects_who_trust(game.subjects , game.traitor)
#trusted = game.subjects_who_are_trusted(game.subjects, game.traitor)
#who_trusts_who = game.who_trusts_who(game.trusting, game.trusted, game.traitor)

#Creates 2 seperate board games
gameboard_1 = board.board_game(game.trusting)
gameboard_2 = board.board_game(game.trusting)

#Prints inital, blankboardgame
board.print_board(gameboard_1, game.subjects)

#Loops game until guess in made
while game.guess is False:
    
    if game.turn % 2 == 0:
        player = 1
    else:
        player = 2
    
    print()
    print("Player " , str(player))    

    answer = questions.choice()
    if answer == 1:
        sub_x = questions.who_to_ask()
        sub_y = questions.do_you_trust(sub_x)
        x_trusts_y = board.sub_x_trusts_sub_y(sub_x, sub_y, game.who_trusts_who )

        if player == 1:
            player_1_board = board.update_board(gameboard_1, sub_x, sub_y, x_trusts_y)
            gameboard_1 = board.board_game(game.trusting)
            board.print_board(player_1_board, game.subjects)
            gameboard_1 = player_1_board
            
        if player == 2:
            player_2_board = board.update_board(gameboard_2, sub_x, sub_y, x_trusts_y)
            gameboard_2 = board.board_game(game.trusting)
            board.print_board(player_2_board, game.subjects)
            gameboard_2 = player_2_board
    
        game.turn+=1
    
    elif answer == 2:
        report_traitor = questions.guess()
        game.guess = game.win(report_traitor, game.traitor)
        
    elif answer == 3:
        game.guess = game.kings_mercy()
    
    if game.guess == True:    
        play_again = questions.continue_quest()
    
        if play_again == True:
            questions.start_game()
            gameboard_1 = board.board_game(game.trusting)
            gameboard_2 = board.board_game(game.trusting)
            board.print_board(gameboard_1, game.subjects)
            game.guess = False