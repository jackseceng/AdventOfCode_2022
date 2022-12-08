with open("input.txt", "r") as ipt:
    score = 0
    for i in ipt:
        if i[2] == 'X':
            score += 1  # Score for what I play
            if i[0] == 'A':
                score += 3  # Score for draw outcome
            if i[0] == 'C':
                score += 6  # Score for win outcome
        elif i[2] == 'Y':
            score += 2
            if i[0] == 'B':
                score += 3  # Score for draw outcome
            if i[0] == 'A':
                score += 6  # Score for win outcome
        elif i[2] == 'Z':
            score += 3
            if i[0] == 'C':
                score += 3  # Score for draw outcome
            if i[0] == 'B':
                score += 6  # Score for win outcome
    print("My total score: " + str(score))
