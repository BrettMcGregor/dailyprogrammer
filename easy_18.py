# Often times in commercials, phone numbers contain letters
# so that they're easy to remember (e.g. 1-800-VERIZON).
# Write a program that will convert a phone number that
# contains letters into a phone number with only numbers
# and the appropriate dash. Click here to learn more about
# the telephone keypad.
#
# Example Execution: Input: 1-800-COMCAST Output: 1-800-266-2278


def phone_number(number):
    keypad = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
              7: "pqrs", 8: "tuv", 9: "wxyz"}
    output = ""
    for char in number:
        if char.isnumeric():
            output += char
        elif char == "-":
            output += char
        elif char.isalpha():
            for k, v in keypad.items():
                if char.lower() in v:
                    output += str(k)
    output = "".join(output[:9]) + "-" + output[9:]
    return output


input = "1-800-COMCAST"
print(phone_number(input))
