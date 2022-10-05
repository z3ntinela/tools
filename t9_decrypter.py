"""
T9 encryption replaces a letter by the corresponding key code on a mobile phone keypad/keyboard
author: CSIRT-EPN
name: t9_decrypter.py
"""
original_flag = ""
t9_dict = {
    "0":" ",
    "2": "a",
    "22": "b",
    "222": "c",
    "3": "d",
    "33": "e",
    "333": "f",
    "4": "g",
    "44": "h",
    "444": "i",
    "5": "j",
    "55": "k",
    "555": "l",
    "6": "m",
    "66": "n",
    "666": "o",
    "7": "p",
    "77": "q",
    "777": "r",
    "7777": "s",
    "8": "t",
    "88": "u",
    "888": "v",
    "9": "w",
    "99": "x",
    "999": "y",
    "9999": "z"
}

def decrypt_t9(message):
    letters_list=[]
    letter_codes = message.strip().split(" ")
    for letter_code in letter_codes:
        if letter_code in t9_dict:
            letters_list.append(t9_dict[letter_code].upper())
        else:
            letters_list.append(letter_code)
    return ''.join(letters_list)


print(original_flag)
print(decrypt_t9(original_flag))
