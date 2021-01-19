import numpy as np
import cv2
from matplotlib import pyplot as plt

DEFAULT_LEN = [35, 265, 932, 2, 49]


"""
Get the color of the stone on the specific square.
Could be black stone, white stone or no stone.
TODO This function definitely needs further improvements.
1 means black, -1 means white, 0 means no stone.
These thresholds are set for fox Go server.
"""


def get_stone_color(square, black_thresh=90, white_thresh=190):
    mean_color = np.mean(square)
    # print(mean_color)
    if mean_color >= white_thresh:
        return -1
    if mean_color <= black_thresh:
        return 1
    return 0


"""
Get game position a Go board image, return an 2d array of numbers(-1, 0 or 1).
Each square could contain black stone, white stone or no stone.
"""


def get_game_position(go_board, edge_len_x, edge_len_y, stone_len, board_size=19):
    rows = cols = board_size
    pos_array = [[0 for i in range(cols)] for j in range(rows)]
    for y in range(board_size):
        for x in range(board_size):
            piece = go_board[edge_len_y + stone_len * y:edge_len_y + stone_len * (y + 1),
                             edge_len_x + stone_len * x:edge_len_x + stone_len * (x + 1)]
            pos_array[y][x] = get_stone_color(piece)
            # print(square_array[y])
            # if x == 18:
            #     cv2.imshow('image', piece)
            #     cv2.waitKey(0)
            #     cv2.destroyAllWindows()
    return pos_array


"""
Get Go board from an image.
"""


def get_go_board(game_image, edge_top, edge_left, board_len_x, board_len_y):

    return game_image[edge_top:edge_top+board_len_y, edge_left:edge_left+board_len_x]



"""
Generate sgf string according to the game position array.
"""


def get_sgf_txt(pos_array, board_size=19):
    black_pos = []
    white_pos = []
    sgf_txt = "(;"
    for i in range(board_size):
        for j in range(board_size):
            if pos_array[i][j] == 1:
                black_pos.append(num_to_letter(j)+num_to_letter(i))
            if pos_array[i][j] == -1:
                white_pos.append(num_to_letter(j)+num_to_letter(i))
    sgf_txt += "AB"
    for pos in black_pos:
        sgf_txt += "[" + pos + "]"
    sgf_txt += "AW"
    for pos in white_pos:
        sgf_txt += "[" + pos + "]"
    sgf_txt += ")"
    return sgf_txt


"""
Transform coordinate(number) to coordinate(letter).
Number should be from 0-18, letter should be a-s.
"""


def num_to_letter(num):
    diff = ord('a') - 0
    return chr(num + diff)



"""
Convert Go game image to an sgf file.
"""


def img_to_sgf(game_image, sgf_file):
    return None


"""
Get the color and the position of the current move
"""


def current_move_info(game_image):
    return None


"""
Show RGB histogram of an image.
"""


def plot_histogram(square):
    color = ('b', 'g', 'r')
    for k, col in enumerate(color):
        hist = cv2.calcHist([square], [k], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])
    plt.show()


# get sgf for image 13
# img = cv2.imread('../images/13.PNG')
#
#
# game_position = get_game_position(img, 49, 49, 94)
#
#
# f = open("out1.sgf", "w")
# f.write(get_sgf_txt(game_position))
# f.close()


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('image_path', help='Specify the path of the Go board image')
parser.add_argument('sgf_path', help='Specify the path of the output SGF file')
parser.add_argument('--default_len', help='if use the default arguments for lengths', action='store_true')
parser.add_argument('-t', help='Specify edge top', type=int)
parser.add_argument('-l', help='Specify edge left', type=int)
parser.add_argument('-b', help='Specify board length', type=int)
parser.add_argument('-e', help='Specify edge length', type=int)
parser.add_argument('-s', help='Specify stone length', type=int)


args = parser.parse_args()

image_path = args.image_path
sgf_path = args.sgf_path

t, l, b, e, s = args.t, args.l, args.b, args.e, args.l

if args.default_len:
    (t, l, b, e, s) = tuple(DEFAULT_LEN)



# Get sgf for fox Go server images
# Still cannot identify current move yet
# Still cannot identify the black/white squares from the mouse

img = cv2.imread(image_path)

# print(np.shape(img))

# get_go_board(game_image, edge_top, edge_left, board_len_x, board_len_y)
board_img = get_go_board(img, t, l, b, b)

# cv2.imshow('image', board_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # get_game_position(go_board, edge_len_x, edge_len_y, stone_len, board_size=19):
game_position = get_game_position(board_img, e, e, s)

f = open(sgf_path, "w")

f.write(get_sgf_txt(game_position))
f.close()


