


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0], ]


def grid(game_map, player=0, row=0, col=0) :
    try:
        print("   a  b  c ")

        if player != 0 :
            game_map[row][col] = player

        for count, row in enumerate(game_map) :
            print(count, row)
        return game_map

    except IndexError as e :
        print("Error. Something went wrong. ", e)
    except Exception as e:
        print("Error: Something went very wrong!", e)



game = grid(game)

game = grid(grid, 1, row=3, col=2)

# single line comment
''' multi
    line
    comment
'''

