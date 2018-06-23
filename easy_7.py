# Write a program that can translate Morse code in the format of
#  ...---...
#
# A space and a slash will be placed between words. ..- / --.-
#
# For bonus, add the capability of going from a string to Morse code.
#
# Super-bonus if your program can flash or beep the Morse.
#
# This is your Morse to translate:

code = (".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / "
        "--. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / "
        "-.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--")

morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
         'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
         'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
         'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
         'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
         '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
         '9':'----.', '0':'-----', ' ':'/'}


def morse_decode(source):
    words = []
    decode = []
    for word in source.split(" / "):
        words.append(word.split(" "))
    for word in words:
        string = ""
        for let in word:
            for k, v in morse.items():
                if let == v:
                    string += k
        decode.append(string.lower())
    return " ".join(decode)


def morse_code(s):
    encode = []

    out_string = ""
    for letter in s:
        for key in morse.keys():
            if letter.upper() == key:
                out_string += f"{morse[key]} "
    encode.append(out_string)

    return " ".join(encode)


# print(morse_code(input("Enter text to convert to Morse code\n> ")))

print(morse_decode(code))
print(morse_code(morse_decode(code)))
print(morse_decode(morse_code(morse_decode(code))))
