with open("input.txt", "r") as ipt:
    score = 0
    for i in ipt:
        if i[2] == 'X':
            # No score for loss
            if i[0] == 'A':
                score += 3  # Score for using scissors
            if i[0] == 'B':
                score += 1  # Score for using rock
            if i[0] == 'C':
                score += 2  # Score for using paper
        elif i[2] == 'Y':
            score += 3  # Score for daw
            if i[0] == 'A':
                score += 1  # Score for using rock
            if i[0] == 'B':
                score += 2  # Score for using paper
            if i[0] == 'C':
                score += 3  # Score for using scissors
        elif i[2] == 'Z':
            score += 6  # Score for win
            if i[0] == 'A':
                score += 2  # Score for using paper
            if i[0] == 'B':
                score += 3  # Score for using scissors
            if i[0] == 'C':
                score += 1  # Score for using rock
    print("My total score: " + str(score))
