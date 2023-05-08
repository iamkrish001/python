
def check_for_win(entries, player):
    # entries: list grid with X's and O's
    # player: string - 'X' or 'O', whoever's turn it is
    if entries[0] == entries[1] == entries[2] == player or \
        entries[3] == entries[4] == entries[5] == player or \
        entries[6] == entries[7] == entries[8] == player:
        return True

    elif entries[0] == entries[3] == entries[6] == player or \
        entries[1] == entries[4] == entries[7] == player or \
        entries[2] == entries[5] == entries[8] == player:
        return True

    elif entries[0] == entries[4] == entries[8] == player or \
        entries[2] == entries[4] == entries[7] == player:
        return True

    return False



if choice in grid_pos:
    t.setpos(grid_pos[choice])
    entries[choice-1] = seal  # new
    t.pd()
    t.write(seal, font = ("Arial",30,"bold"))
    if check_for_win(grid_pos, seal):  # new
        has_won(seal)

grid_choices = [1,2,3,4,5,6,7,8,9]
entries = 9*[0]  # new

def has_won(player):  # new
    print("Congrats %s's, you have won!" % seal)  # new


