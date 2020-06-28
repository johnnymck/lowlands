from models import gameboard, windmill
from views.landview import print_land

def main():
    board = gameboard.GameBoard(10,10)
    asset = windmill.Windmill()
    board.set_board(0,0, asset)
    board.set_board(2,7, windmill.Windmill())
    board.set_board(9,10, windmill.Windmill())
    print_land(board.get_board())

if __name__ == '__main__':
    main()