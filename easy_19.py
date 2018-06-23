# Challenge #19 will use The Adventures of Sherlock Holmes
# from Project Gutenberg.
#
# Write a program that counts the number of alphanumeric
# characters there are in The Adventures of Sherlock Holmes.
# Exclude the Project Gutenberg header and footer, book title,
# story titles, and chapters. Post your code and the
# alphanumeric character count.

with open("pg1661.txt") as file:
    count = 0
    for i in range(61):
        next(file)
    while True:
        if "End of the Project Gutenberg EBook" in file.readline():
            break
        else:
            x = file.readline()
            for char in x:
                if char.isalnum():
                    count += 1
    print(count)


    # while True:
    #     if "End of the Project Gutenberg EBook" in file.readline():
    #         break
    #     else:
    #         content.append(file.readline())
    #     print(content)