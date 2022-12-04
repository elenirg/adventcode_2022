
# First Column: A for Rock, B for Paper, and C for Scissors. 
# Second column: X for Rock, Y for Paper, and Z for Scissors.

# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
# 1 for Rock, 2 for Paper, and 3 for Scissors

score = 0
hand = []

with open('input.txt', 'r') as fp:
    for line in fp:
        hand = line.split()
        print(line)
        print(hand)
        # if ((hand[0] == 'A') and (hand[1] == 'X')) or ((hand[0] == 'B') and (hand[1] == 'Y')) or ((hand[0] == 'C') and (hand[1] == 'Z')) :
        #     # 3 if the round was a draw
        #     score += 3 
        #     if (hand[1] == 'X') :
        #         score += 1
        #     elif (hand[1] == 'Y') :
        #         score += 2
        #     elif (hand[1] == 'Z') :
        #         score += 3
        #     else:
        #         print('Hand is not recognized')
        # elif () :
        #     #  0 round I lost
        #     score += 0
        # elif () :
        #     #  6 round I won 
        #     score += 6  
        # else :
        #     print('Round result is not recognized')   


        if ( hand[1] == 'X' ) :
            score += 1   

            if ( hand[0] == 'A' ) :
            # check if draw
                score += 3
            elif ( hand[0] == 'B' ) :
            # check if lost
                score += 0
            elif ( hand[0] == 'C' ) :
            # check if win
                score += 6

        elif  ( hand[1] == 'Y' ) :
            score += 2

            if ( hand[0] == 'A' ) :
            # check if win
                score += 6
            elif ( hand[0] == 'B' ) :
            # check if draw
                score += 3
            elif ( hand[0] == 'C' ) :
            # check if lost
                score += 0

        elif  ( hand[1] == 'Z' ) :
            score += 3

            if ( hand[0] == 'A' ) :
            # check if lost
                score += 0
            elif ( hand[0] == 'B' ) :
            # check if win
                score += 6
            elif ( hand[0] == 'C' ) :
            # check if draw
                score += 3

        else :
           print('Hand is not recognized') 


print ('Score is: ', score)