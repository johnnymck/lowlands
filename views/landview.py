"""Landview.py
Pretty display land in-game to screen
"""

def print_land(gameboard):
    for i in range(len(gameboard[0])+2):
        print("- ", end="")
    print()
    for i, row in enumerate(gameboard):
        print("| ", end="")
        for j, col in enumerate(row):
            # print symbols:
            current_symbol = ""
            current_level = gameboard[j][i]._height
            if  gameboard[j][i]._structure != None:
                current_symbol = 'W'
            elif current_level < -5:
                current_symbol = "≈"
            elif current_level < 5:
                current_symbol = "~"
            elif current_level < 10:
                current_symbol = "."
            elif current_level < 20:
                current_symbol = "o"
            elif current_level < 40:
                current_symbol = '*'
            elif current_level <= 100:
                current_symbol = '@'
            else:
                current_sumbol = "W"
            print((current_symbol + " "), end="")
        print("|")
    for i in range(len(gameboard[0])+2):
        print("- ", end="")
    print()
    