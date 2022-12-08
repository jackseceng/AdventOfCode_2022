def extract_ascii(char1):
    if ord(char1) in range(65, 90):  # Check if character is in upper case range of ASCII decimal
        return int(ord(char1) - 38)  # Return ASCII reference decimal, minus 38 to match priority range
    elif ord(char1) in range(97, 122):  # Check if character is in lower case range of ASCII decimal
        return int(ord(char1) - 96)  # Return ASCII reference decimal, minus 96 to match priority range
    else:
        return 0


with open("input.txt", "r") as ipt:
    priority_sum = 0
    for i in ipt:
        first = (i[0:(len(i) // 2)])  # First character to character at half the length of string
        second = (i[(len(i) // 2):len(i)])  # Character at half the length of string to character at length of string
        for j in first:  # Loop through elements of first half
            if j in second:  # Check for duplicates of elements in first half within second half
                priority = extract_ascii(j)  # Extract priority number from function
                priority_sum += priority  # Sum the total priority so far with the newly extracted priority number
                break  # Stop looping through current ipt
            else:
                continue  # No match, continue loops
    print(priority_sum)
