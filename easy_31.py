# Write a function that takes two base-26 numbers
# in which digits are represented by letters with
# A=0, B=1, … Z=25 and returns their product using
# the same notation. As an example, CSGHJ × CBA = FNEUZJA.
#
# Your task is to write the base-26 multiplication function.
#
# Try to be very efficient in your code!
#
# I found this challenge to be extraordinarily diffcult!!!


def multiply_alphabet(a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = []
    y = []
    j = len(a) - 1
    for i in range(len(a)):
        x.append(alphabet.index(a[i].lower())*26**j)
        j -= 1
    # print(f"{a} (10)", sum(x))
    k = len(b) - 1
    for m in range(len(b)):
        y.append(alphabet.index(b[m].lower())*26**k)
        k -= 1
    # print(f"{b} (10)", sum(y))

    base10 = sum(x)*sum(y)  # answer in base 10

    # convert base 10 to base 26
    # find maximum power of 26 divisible into base10
    power = 10
    result = []
    while power >= 0:
        if 26 ** power > base10 + 1:
            power -= 1
        else:
            result.append(alphabet[int((base10 // 26 ** power))].upper())
            base10 = base10 - ((base10 // 26 ** power) * 26 ** power)
            power -= 1
    return "".join(result)


print(multiply_alphabet("CSGHJ", "CBA"))


# print("FNEUZJA (base10) =",f"{(5*26**6)+(13*26**5)+(4*26**4)+(20*26**3)+(25*26**2)+(9*26**1)+(0*26**0)}")
#
# print("CSGHJ (base26) =", "218679")
# print("CSGHJ (base10) =", f"{2*26**4+18*26**3+6*26**2+7*26**1+9*26**0}")
# print("CBA (base26) =", "210")
# print("CBA (base10) =", f"{2*26**2+1*26**1+0*26**0}")
#
#
# print("CSGHJ * CBA (base10) = ",(1234567 * 1378))
#
# print("CSGHJ * CBA (base26) = ", 5134202590)
#
#
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
