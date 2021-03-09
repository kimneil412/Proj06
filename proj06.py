#####################################################
# Computer Project #6
# Neil Kim
# Algorithms
# Open CSV file
# Make definitions for different types of functions
# Asks to input text
# Prompt for inputs
# Using the text spits out information
# Positions for players
#####################################################
import csv


#This function takes no arguments, prompts for a file name and returns the file pointer to
#that file
def open_file():
    try:
        input_file = input("Enter filename: ")
        open(input_file, 'r')
        return input_file
    except:
        FileNotFoundError
    pass

#This function accepts a file pointer and returns a master list of lists of all the data in the
#file
def read_file(fp):
    r = csv.reader(fp)
    lists = []
    next(r, None)
    for line in r:
        lists.append(line)
    return lists
    pass

#This function accepts as input the master list and returns two integers representing the
#count of players who shoot left and those who shoot right
def shoots_left_right(master_list):
    left = 0
    right = 0
    for i in master_list:
        if i[1] == 'L':
            left += 1
        else:
            i[1] == 'R'
            right += 1
    return left, right
    pass

#This function accepts as input the master list and returns four integers representing the
#count of players who play positions left-wing, right-wing, center, and
#defense
def position(master_list):
    center = 0
    defense = 0
    left = 0
    right = 0
    for i in master_list:
        if i[2] == 'C':
            center += 1
        elif i[2] == 'D':
            defense += 1
        elif i[2] == 'L':
            left += 1
        else:
            i[2] == 'R'
            right += 1
    return left, right, center, defense
    pass

#This function accepts as input the master list and returns two integers representing the
#count of players who play the left-wing position but shoot right and those who
#play the right-wing position but shoot left
def off_side_shooter(master_list):
    left = 0
    right = 0
    for i in master_list:
        if i[1] == 'L' and i[2] == 'R':
            right += 1
        elif i[1] == 'R' and i[2] == 'L':
            left += 1
    return left, right
    pass

#This function accepts as input the master list and returns two integers representing the
#count of players who play the left-wing position but shoot right and those who
#play the right-wing position but shoot left
def points_per_game(master_list):
    tuples = []
    for i in master_list:
        name = i[0]
        points = i[18]
        points = points.replace(",","")
        points = float(points)
        pos = i[2]
        tuple = (points,name,pos)
        tuples.append(tuple)
    tuples.sort(reverse=True)
    return tuples[0:10]
    pass

#This function accepts as input the master list and returns a sorted list of tuples where each
#tuple is of the form: (games played, player name)
def games_played(master_list):
    tuples = []
    for i in master_list:
        name = i[0]
        games = i[3]
        games = games.replace(",","")
        games = int(games)
        tuple = (games, name)
        tuples.append(tuple)
    tuples.sort(reverse=True)
    return tuples[0:10]
    pass

#This function accepts as input the master list and returns a sorted list of tuples where each
#tuple is of the form: (shots taken, player name)
def shots_taken(master_list):
    tuples = []
    for i in master_list:
        for x in ",":
            i[9] = str(i[9])
            i[9] = i[9].replace(x, '')
        if i[9] == '--':
            i[9] = 0
        i[9] = int(i[9])
        tuple = (i[9], i[0])
        tuples.append(tuple)
    tuples.sort(reverse=True)
    return tuples[0:10]
    pass

def main():
    fp = open_file()
    stat = open(fp, 'r')
    stat = read_file(stat)

    print('')
    print('')
    print(' ' + 'Shooting ')
    print("{:<10s}{:<15,d}".format('left:', shoots_left_right(stat)[0]))
    print("{:<10s}{:<15,d}".format('right:', shoots_left_right(stat)[1]))
    print('')

    print('  ' + 'Position  ')
    print("{:<10s}{:<20,d}".format('left:', position(stat)[0]))
    print("{:<10s}{:<20,d}".format('right:', position(stat)[1]))
    print("{:<10s}{:<20,d}".format('center:', position(stat)[2]))
    print("{:<10s}{:<20,d}".format('defense:', position(stat)[3]))
    print('')

    print('    ' + 'Off-side Shooter    ')
    print("{:<22s}{:>14,d}".format('left-wing shooting right:', off_side_shooter(stat)[0]))
    print("{:<22s}{:>14,d}".format('right-wing shooting left:', off_side_shooter(stat)[1]))
    print('')

    print('      ' + 'Top Ten Points-Per-Game')
    print("{:<20s}{:>5s}".format('Player', 'Position Points Per Game'))

    print("{:<20s}{:>5s}{:>16.2f}".format(points_per_game(stat)[0][1], points_per_game(stat)[0][2],
                                          points_per_game(stat)[0][0]))
    print("{:<20s}{:>5s}{:>16.2f}".format(points_per_game(stat)[1][1], points_per_game(stat)[1][2],
                                          points_per_game(stat)[1][0]))
    print("{:<20s}{:>5s}{:>16.2f}".format(points_per_game(stat)[2][1], points_per_game(stat)[2][2],
                                          points_per_game(stat)[2][0]))
    print("{:<20s}{:>5s}{:>16.2f}".format(points_per_game(stat)[3][1], points_per_game(stat)[3][2],
                                          points_per_game(stat)[3][0]))
    print("{:<20s}{:>5s}{:>16.2f}".format(points_per_game(stat)[4][1], points_per_game(stat)[4][2],
                                          points_per_game(stat)[4][0]))
    print("{:<20s}{:>5s}{:>16.2f}".format(points_per_game(stat)[5][1], points_per_game(stat)[5][2],
                                          points_per_game(stat)[5][0]))
    print("{:<20s}{:>5s}{:>16.2f}".format(points_per_game(stat)[6][1], points_per_game(stat)[6][2],
                                          points_per_game(stat)[6][0]))
    print("{:<20s}{:>5s}{:>16.2f}".format(points_per_game(stat)[7][1], points_per_game(stat)[7][2],
                                          points_per_game(stat)[7][0]))
    print("{:<20s}{:>5s}{:>16.2f}".format(points_per_game(stat)[8][1], points_per_game(stat)[8][2],
                                          points_per_game(stat)[8][0]))
    print("{:<20s}{:>5s}{:>16.2f}".format(points_per_game(stat)[9][1], points_per_game(stat)[9][2],
                                          points_per_game(stat)[9][0]))

    print('')
    print('        ' + 'Top Ten Games-Played')
    print("{:<22s}{:>14s}".format('Player', 'Games Played'))

    print("{:<22s}{:>14,d}".format(games_played(stat)[0][1], games_played(stat)[0][0]))
    print("{:<22s}{:>14,d}".format(games_played(stat)[1][1], games_played(stat)[1][0]))
    print("{:<22s}{:>14,d}".format(games_played(stat)[2][1], games_played(stat)[2][0]))
    print("{:<22s}{:>14,d}".format(games_played(stat)[3][1], games_played(stat)[3][0]))
    print("{:<22s}{:>14,d}".format(games_played(stat)[4][1], games_played(stat)[4][0]))
    print("{:<22s}{:>14,d}".format(games_played(stat)[5][1], games_played(stat)[5][0]))
    print("{:<22s}{:>14,d}".format(games_played(stat)[6][1], games_played(stat)[6][0]))
    print("{:<22s}{:>14,d}".format(games_played(stat)[7][1], games_played(stat)[7][0]))
    print("{:<22s}{:>14,d}".format(games_played(stat)[8][1], games_played(stat)[8][0]))
    print("{:<22s}{:>14,d}".format(games_played(stat)[9][1], games_played(stat)[9][0]))


    print('')
    print('        ' + 'Top Ten Shots-Taken')
    print("{:<22s}{:>14s}".format('Player', 'Shots Taken'))
    a = 0

    print("{:<22s}{:>14,d}".format(shots_taken(stat)[0][1], shots_taken(stat)[0][0]))
    print("{:<22s}{:>14,d}".format(shots_taken(stat)[1][1], shots_taken(stat)[1][0]))
    print("{:<22s}{:>14,d}".format(shots_taken(stat)[2][1], shots_taken(stat)[2][0]))
    print("{:<22s}{:>14,d}".format(shots_taken(stat)[3][1], shots_taken(stat)[3][0]))
    print("{:<22s}{:>14,d}".format(shots_taken(stat)[4][1], shots_taken(stat)[4][0]))
    print("{:<22s}{:>14,d}".format(shots_taken(stat)[5][1], shots_taken(stat)[5][0]))
    print("{:<22s}{:>14,d}".format(shots_taken(stat)[6][1], shots_taken(stat)[6][0]))
    print("{:<22s}{:>14,d}".format(shots_taken(stat)[7][1], shots_taken(stat)[7][0]))
    print("{:<22s}{:>14,d}".format(shots_taken(stat)[8][1], shots_taken(stat)[8][0]))
    print("{:<22s}{:>14,d}".format(shots_taken(stat)[9][1], shots_taken(stat)[9][0]))

    pass

if __name__ == "__main__":
    main()
