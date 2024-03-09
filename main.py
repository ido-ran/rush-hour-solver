board = \
"""********
*  O AA*
*  O   *
*XXO   V
*PPP  Q*
*     Q*
*     Q*
********"""
board = board.split("\n")


cars = [
    {"tag": "A", "dir": "hor"},
    {"tag": "O", "dir": "ver"},
    {"tag": "Q", "dir": "ver"},
    {"tag": "P", "dir": "hor"},
    {"tag": "X", "dir": "hor"},
]

for row in range(8):
    for col in range(8):
        if board[row][col] == "X":
            print([row,col])

# for car in cars:
#     if car["dir"] == "hor":
#         print("horisantal", car["tag"])
#     else:
#         print("vertical", car["tag"])
