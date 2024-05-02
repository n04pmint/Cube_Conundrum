
#PART 1

# total = 0

# for index, line in enumerate(open("input/input.txt")):
#     group = line.strip().split(": ")[1].split("; ")
#     for g in group:
#         input_map = {"red": 0, "green": 0, "blue": 0}
#         for each in g.split(", "):
#             number, color = each.split()
#             input_map[color] = int(number)
#         if input_map["red"] > 12 or input_map["green"] > 13 or input_map["blue"] > 14:
#             break
#     else:
#         total += index + 1

# print(total)


#PART 2----------------------------------------------------------------------------

total = 0

for index, line in enumerate(open("input/input.txt")):
    group = line.strip().split(": ")[1].split("; ")
    total_map = {"red": 0, "green": 0, "blue": 0}
    for g in group:
        input_map = {"red": 0, "green": 0, "blue": 0}
        for each in g.split(", "):
            number, color = each.split()
            input_map[color] = int(number)
        for c in total_map:
            total_map[c] = max(total_map[c], input_map[c])
    total += total_map["red"] * total_map["green"] * total_map["blue"]

print(total)