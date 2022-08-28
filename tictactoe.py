playing_field = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]

def detect_win(field):
    for i, arr in enumerate(field):
        if arr[0] == arr[1] == arr[2] == 1:
            return True
        elif field[0][i] == field[1][i] == field[2][i] == 1:
            return True
        elif field[0][0] == field[1][1] == field[2][2] == 1 or field[0][2] == field[1][1] == field[2][0] == 1:
            return True
        elif arr[0] == arr[1] == arr[2] == -1:
            return False
        elif field[0][i] == field[1][i] == field[2][i] == -1:
            return False
        elif field[0][0] == field[1][1] == field[2][2] == -1 or field[0][2] == field[1][1] == field[2][0] == -1:
            return False
    return None

starting_pos_value = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

def brute_force(playing_field, starting_pos):
    playing_field[starting_pos[0]][starting_pos[1]] = 1
    for arr in playing_field:
        for i, value in enumerate(arr):
            if value == None and sum(playing_field)/len(playing_field) > 0:
                arr[i] = 1
            elif value == None and sum(playing_field)/len(playing_field) <= 0:
                arr[i] = 0

            if detect_win(playing_field) == None:
                bruteforce(playing_field)
            else:
                starting_pos_value[starting_pos[0]][starting_pos[1]] += detect_win(playin_field)

brute_force(playing_field, [0, 0])
