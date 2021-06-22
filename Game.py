theBoard = {1: ' ' , 2: ' ' , 3: ' ' ,
            4: ' ' , 5: ' ' , 6: ' ' ,
            7: ' ' , 8: ' ' , 9: ' ' }

WIN_MESSAGE = " won. ***"
FINISH = "\nGame Over\n"

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

board_keys = []

for key in theBoard:
    board_keys.append(key)

# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0
    
    # print("Board Layout:\n")
    # print('1' + '|' + '2' + '|' + '3')
    # print('-+-+-')
    # print('4' + '|' + '5' + '|' + '6')
    # print('-+-+-')
    # print('7' + '|' + '8' + '|' + '9')

    for i in range(10):
        printBoard(theBoard)
        print("It's "+ turn + "s turn. Which place to mark ?!")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already marked. Try Another.\n")
            continue
        
        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard[1] == theBoard[2] == theBoard[3] != ' ':
                printBoard(theBoard)
                print(FINISH)
                print("***" + turn + WIN_MESSAGE)
                break
            elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':
                printBoard(theBoard)
                print(FINISH)
                print("***" + turn + WIN_MESSAGE)
                break
            elif theBoard[7] == theBoard[8] == theBoard[9] != ' ':
                printBoard(theBoard)
                print(FINISH)
                print("***" + turn + WIN_MESSAGE)
                break
            elif theBoard[1] == theBoard[4] == theBoard[7] != ' ':
                printBoard(theBoard)
                print(FINISH)
                print("***" + turn + WIN_MESSAGE)
                break
            elif theBoard[2] == theBoard[5] == theBoard[8] != ' ':
                printBoard(theBoard)
                print(FINISH)
                print("***" + turn + WIN_MESSAGE)
                break
            elif theBoard[3] == theBoard[6] == theBoard[9] != ' ':
                printBoard(theBoard)
                print(FINISH)
                print("***" + turn + WIN_MESSAGE)
                break
            elif theBoard[7] == theBoard[5] == theBoard[3] != ' ':
                printBoard(theBoard)
                print(FINISH)
                print("***" + turn + WIN_MESSAGE)
                break
            elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':
                printBoard(theBoard)
                print(FINISH)
                print("***" + turn + WIN_MESSAGE)
                break
    
        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print(FINISH)
            print("It's a Tie!\nDon't Worry... It's quite common")
        
        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.
    restart = input("Wanna give it another go ?! (y/n)")

    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theBoard[key] = ' '
        game()
    else:
        print("Cools! Have a Great Day!\n")
        

if __name__ == "__main__":
    game()