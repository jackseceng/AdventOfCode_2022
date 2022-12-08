with open("input.txt", "r") as ipt:
    elf_cals = []
    cur_cal = 0
    for i in ipt:
        if any(chr.isdigit() for chr in i):
            cur_cal += int(i)
        else:
            elf_cals.append(cur_cal)
            cur_cal = 0
    n = len(elf_cals)
    elf_cals.sort()
    print("Most calories carried by 1 elf: " + str(elf_cals[n-1]))
    print("Most calories carried by top 3 elfs: " + str(elf_cals[n-1] + elf_cals[n-2] + elf_cals[n-3]))
