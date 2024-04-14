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

def find_car(tag):
    pos = []
    for row in range(8):
        for col in range(8):
            if board[row][col] == tag:
                pos.append([row,col])

    return pos

print(find_car("P"))
print(find_car("O"))
print(find_car("A"))
print(find_car("Q"))
print(find_car("X"))

# for car in cars:
#     if car["dir"] == "hor":
#         print("horisantal", car["tag"])
#     else:
#         print("vertical", car["tag"])
