import sys

for i in sys.argv[1:]:
    if len(i) == 9:
        input_board = i
    else: 
        input_board = '.........'
    if len(i) == 1:
        try:
            int(i)
            game_number = i
        except:
            token = i
