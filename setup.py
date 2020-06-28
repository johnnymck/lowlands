from models import gameboard

def main():
    board = gameboard.GameBoard(10,10)
    print(len(board.get_board()))

if __name__ == '__main__':
    main()