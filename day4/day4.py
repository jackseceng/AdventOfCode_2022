def is_contained_range(assignment):
    start, end = assignment.split(',')  # Create start and end of assignment pair
    p1s, p1e = start.split('-')  # Create start and end of first assignment
    p2s, p2e = end.split('-')  # Create start and end of second assignment
    if int(p1s) <= int(p2s) and int(p1e) >= int(p2e):  # Check if the 2 pairs have equal or inclusive starts or ends
        return True
    elif int(p2s) <= int(p1s) and int(p2e) >= int(p1e):  # Check if the 2 pairs have equal or inclusive starts or ends
        return True


def is_overlapping_assignment(assignment):
    start, end = assignment.split(',')  # Create start and end of assignment pair
    p1s, p1e = start.split('-')  # Create start and end of first assignment
    p2s, p2e = end.split('-')  # Create start and end of second assignment
    for i in range(int(p1s), int(p1e) + 1):  # Loop through first assignment as a range
        if i in range(int(p2s), int(p2e) + 1):  # Check if any element of the second assignment is in the first
            return True


with open("input.txt", "r") as assignments:  # Open puzzle input as .txt file
    contained_ranges = 0  # Initiate counter for contained ranges result
    overlapping_assignments = 0
    for assignment in assignments:  # Loop through each line in puzzle input
        if is_contained_range(assignment):  # Check if the pair overlap using split_assignment function
            contained_ranges += 1  # Increment the counter for contained ranges
        if is_overlapping_assignment(assignment):
            overlapping_assignments += 1
        else:
            continue  # If statement false, don't increment counter, continue for loop
    print(contained_ranges)  # Print result of contained ranges calculation
    print(overlapping_assignments)  # Print results of overlapping assignments calculation
