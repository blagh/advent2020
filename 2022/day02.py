
THEM_ROCK = "A"
THEM_PAPR = "B"
THEM_SCSR = "C"

MY_ROCK = "X"
MY_PAPR = "Y"
MY_SCSR = "Z"

SHAPE_SCORE = {MY_ROCK: 1, MY_PAPR: 2, MY_SCSR: 3}

WONN = 6
DRAW = 3
LOST = 0

ROUND_SCORE = {
    MY_ROCK: {
        THEM_ROCK: DRAW,
        THEM_PAPR: LOST,
        THEM_SCSR: WONN
    },
    MY_PAPR: {
        THEM_ROCK: WONN,
        THEM_PAPR: DRAW,
        THEM_SCSR: LOST        
    },
    MY_SCSR: {
        THEM_ROCK: LOST,
        THEM_PAPR: WONN,
        THEM_SCSR: DRAW         
    }
}

print(ROUND_SCORE)

def round_score(their_choice, my_choice):
    print(their_choice, my_choice)
    print(SHAPE_SCORE[my_choice])
    print(ROUND_SCORE[my_choice][their_choice])
    return SHAPE_SCORE[my_choice] + ROUND_SCORE[my_choice][their_choice]

MY_LOSS = "X"
MY_DRAW = "Y"
MY_WONN = "Z"

ROUND_SCORE_2 = {MY_LOSS: LOST, MY_DRAW: DRAW, MY_WONN: WONN}

MY_MOVE = {
    MY_LOSS: {
        THEM_ROCK: MY_SCSR,
        THEM_PAPR: MY_ROCK,
        THEM_SCSR: MY_PAPR
    },
    MY_DRAW: {
        THEM_ROCK: MY_ROCK,
        THEM_PAPR: MY_PAPR,
        THEM_SCSR: MY_SCSR        
    },
    MY_WONN: {
        THEM_ROCK: MY_PAPR,
        THEM_PAPR: MY_SCSR,
        THEM_SCSR: MY_ROCK         
    }
}

print(MY_MOVE)

def round_score_2(their_choice, my_outcome):
    print(their_choice, my_outcome)
    my_choice = MY_MOVE[my_outcome][their_choice]
    print(MY_MOVE[my_outcome][their_choice])
    return SHAPE_SCORE[my_choice] + ROUND_SCORE_2[my_outcome]

score = 0
with open("day02input.txt") as file:
    for line in file.readlines():
        their_choice, my_choice = line[0:-1].split(" ")
        score += round_score_2(their_choice, my_choice)

print(score)