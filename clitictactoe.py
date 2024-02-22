import time

def Banner():
  print(" /$$$$$$$$ /$$               /$$$$$$$$                      /$$$$$$$$                 ")  
  print("|__  $$__/|__/              |__  $$__/                     |__  $$__/                 ")
  print("   | $$    /$$  /$$$$$$$       | $$  /$$$$$$   /$$$$$$$       | $$  /$$$$$$   /$$$$$$ ")
  print("   | $$   | $$ /$$_____//$$$$$$| $$ |____  $$ /$$_____//$$$$$$| $$ /$$__  $$ /$$__  $$")
  print("   | $$   | $$| $$     |______/| $$  /$$$$$$$| $$     |______/| $$| $$  \ $$| $$$$$$$$")
  print("   | $$   | $$| $$             | $$ /$$__  $$| $$             | $$| $$  | $$| $$_____/")
  print("   | $$   | $$|  $$$$$$$       | $$|  $$$$$$$|  $$$$$$$       | $$|  $$$$$$/|  $$$$$$$")
  print("   |__/   |__/ \_______/       |__/ \_______/ \_______/       |__/ \______/  \_______/")
  print("                                                                                      ")
  print("    Welcome to the Tic-Tac_tor Game.")      
  print("    This is a two player game.")  
  print("    Enter position as, for example for top left, enter: tl. ")      
  print("    Enter position as, for example for very middle, enter: mm. ")      
  print("\n")                                          



def NewBoard(tl, tm, tr, ml, mm, mr, bl, bm, br):
  print("    -----------------------------------")
  print("              |            |           ")
  print(f"         {tl}    |     {tm}      |     {tr}    ")
  print("              |            |           ")
  print("    -----------------------------------")
  print("              |            |           ")
  print(f"         {ml}    |      {mm}     |      {mr}    ")
  print("              |            |           ")
  print("    -----------------------------------")
  print("              |            |           ")
  print(f"         {bl}    |      {bm}     |      {br}   ")
  print("              |            |           ")
  print("    -----------------------------------")


def win_check(board):

  # Horizontal Wins

  if board[0] == board[1] == board[2] != " ":
    win = True
  elif board[3] == board[4] == board[5] != " ":
    win = True
  elif board[6] == board[7] == board[8] != " ":
    win = True

  # Vertical Wins

  elif board[0] == board[3] == board[6] != " ":
    win = True
  elif board[1] == board[4] == board[7] != " ":
    win = True
  elif board[2] == board[5] == board[8] != " ":
    win = True

  # Diagonal Wins

  elif board[0] == board[4] == board[8] != " ":
    win = True
  elif board[2] == board[4] == board[6] != " ":
    win = True

  # Tie

  elif " " not in board:
    win = None

  # No Wins
  else:
    win = False

  return win
    

def insert_move(board, space, player_char, current_player):
  global invalid_pos

  if not len(space) or len(space) < 2:
    invalid_pos = True
    print("    Invalid position!")
    return

  if space[0] == "t":

    if space[1] == "l" and board[0] == " ":
      board[0] = player_char
      invalid_pos = False
    elif space[1] == "m" and board[1] == " ":
      board[1] = player_char
      invalid_pos = False
    elif space[1] == "r" and board[2] == " ":
      board[2] = player_char
      invalid_pos = False
    else:
      invalid_pos = True
      print("    Invalid position!")

  elif space[0] == "m":

    if space[1] == "l" and board[3] == " ":
      board[3] = player_char
      invalid_pos = False
    elif space[1] == "m" and board[4] == " ":
      board[4] = player_char
      invalid_pos = False
    elif space[1] == "r" and board[5] == " ":
      board[5] = player_char
      invalid_pos = False
    else:
      invalid_pos = True
      print("    Invalid position!")

  elif space[0] == "b":

    if space[1] == "l" and board[6] == " ":
      board[6] = player_char
      invalid_pos = False
    elif space[1] == "m" and board[7] == " ":
      board[7] = player_char
      invalid_pos = False
    elif space[1] == "r" and board[8] == " ":
      board[8] = player_char
      invalid_pos = False
    else:
      invalid_pos = True
      print("    Invalid position!")

  else:
    invalid_pos = True
    print("    Invalid position!")



def get_input(board, current_player, player_one_char, player_two_char):
  if current_player == "Player One":
    space = input("    Player 1, Enter position: ")
    insert_move(board, space, player_one_char, current_player)
    if not invalid_pos:
      current_player = "Player Two"
  else:
    space = input("    Player 2, Enter position: ")
    insert_move(board, space, player_two_char, current_player)
    if not invalid_pos:
      current_player = "Player One"

  return current_player


def validate_chars(player_one_char, player_two_char):
  if player_one_char == player_two_char:
    valid_chars = False
  elif player_one_char != "X" and player_one_char != "O":
    valid_char = False
  elif player_two_char != "X" and player_two_char != "O":
    valid_char = False
  else:
    valid_char = True
  
  return valid_char


def main():
  Banner()
  playing = True

  while True:

    if not playing:
      again = input("    Would you like to play again? (y, n): ")
      if again == "n":
        quit()
      if again == "y":
        playing = True

    player_one_char = input("    Player 1, Choose X or O: ")
    player_two_char = input("    Player 2, Choose X or O: ")

    if not validate_chars(player_one_char, player_two_char):
      print("    Invalid choice")
      time.sleep(5)
      quit()

    global current_player
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "Player One"


    if playing:
      while True:
        NewBoard(board[0], board[1], board[2], board[3], board[4], board[5], board[6],board[7], board[8])
        if win_check(board):
          if current_player == "Player One":
            print("    Player 1 Has Won! Congrats!")
            playing = False
            break
          elif current_player == "Player Two":
            print("    Player 2 Has Won! Congrats!")
            playing = False
            break
        elif win_check(board) == False:
          pass
        else:
          print("    Tie Game!")
          playing = False
          break

        current_player = get_input(board, current_player, player_one_char, player_two_char)


if __name__ == "__main__":
  main()
