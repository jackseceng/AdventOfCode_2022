def extract_ascii(char):
    if ord(char) in range(65, 91):  # Check if character is in upper case range of ASCII decimal
        return int(ord(char) - 38)  # Return ASCII reference decimal, minus 38 to match priority range
    elif ord(char) in range(97, 123):  # Check if character is in lower case range of ASCII decimal
        return int(ord(char) - 96)  # Return ASCII reference decimal, minus 96 to match priority range
    else:
        return 0


def calculate_priority(items):
    first = (items[0:(len(items) // 2)])  # First character to character at half the length of string
    second = (items[(len(items) // 2):len(items)])
    # Character at half the length of string to character at length of string
    for char in first:  # Loop through elements of first half
        if char in second:  # Check for duplicates of elements in first half within second half
            return extract_ascii(char)  # Return priority number
        else:
            continue  # No match, continue loops


def find_common_items(list_of_3):
    for char in list_of_3[0]:
        if char in list_of_3[1] and char in list_of_3[2]:
            return char


with open("input.txt", "r") as ipt:
    priority_sum = 0
    type_priority_sum = 0
    group_list = []
    for item in ipt:  # For each element in the input file
        priority = calculate_priority(item)
        priority_sum += priority  # Sum the total priority so far with the newly extracted priority number
        group_list.append(item.strip('\n'))  # Remove new line characters, and append item to list
        if len(group_list) == 3:  # Once a group of 3 is in a list, begin common item priorities
            common_type_priority = extract_ascii(find_common_items(group_list))
            type_priority_sum += common_type_priority
            # Sum the total type priority so far with the newly calculated priority of the 3 items
            group_list = []  # Reset list
    print(f"Priority sum of each rucksack: {priority_sum}")
    print(f"Priority sum of each group of 3 common items: {type_priority_sum}")

