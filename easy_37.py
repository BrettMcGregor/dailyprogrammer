# write a program that takes
#
# input : a file as an argument
#
# output: counts the total number of lines.
#
# for bonus, also count the number of words in the file.


def file_stats(f):
    with open(f"{f}", encoding='utf-8') as file:
        lines = []
        count = 0
        for line in file.readlines():
            lines.append(line)
        num_lines = len(lines)
        for line in lines:
            for word in line:
                count += 1
        return num_lines, count


print(file_stats("poem.txt"))
