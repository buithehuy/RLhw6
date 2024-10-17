def get_board_size():
    print('Choose size of board 4 or 5')
    sizeboard = int(input())
    if sizeboard != 4 and sizeboard != 5:
        print('Invalid value, choose again')
        return get_board_size()
    else:
        return sizeboard