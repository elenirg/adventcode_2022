
# First Column: A for Rock, B for Paper, and C for Scissors. 
# Second Column: how the round needs to end: 
# X means you need to lose, Y means you need to draw, and Z means you need to win

# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
# 1 for Rock, 2 for Paper, and 3 for Scissors

score = 0
hand = []

with open('input.txt', 'r') as fp:
    for line in fp:
        hand = line.split()
        print(line)
        print(hand)

        if ( hand[1] == 'X' ) :
            # lose
            score += 0   

            if ( hand[0] == 'A' ) :
            # rock - scissors
                score += 3
            elif ( hand[0] == 'B' ) :
            # paper - rock
                score += 1
            elif ( hand[0] == 'C' ) :
            # scissorz - paper
                score += 2

        elif  ( hand[1] == 'Y' ) :
            # draw
            score += 3

            if ( hand[0] == 'A' ) :
            # rock - rock 
                score += 1
            elif ( hand[0] == 'B' ) :
            # paper - paper
                score += 2
            elif ( hand[0] == 'C' ) :
            # scissorz - scissorz
                score += 3

        elif  ( hand[1] == 'Z' ) :
            # win
            score += 6

            if ( hand[0] == 'A' ) :
            # rock - paper
                score += 2
            elif ( hand[0] == 'B' ) :
            # paper - scizzors
                score += 3
            elif ( hand[0] == 'C' ) :
            # scissors - rock
                score += 1

        else :
           print('Hand is not recognized') 


print ('Score is: ', score)