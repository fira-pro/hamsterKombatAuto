# Python program to implement Morse Code Translator
# Source Geeks for geeks

import base64

"""
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
"""

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


class Morse:
    # Function to encrypt the string
    # according to the morse code chart

    @staticmethod
    def encrypt(message):
        cipher = ""
        for letter in message:
            if letter != " ":

                # Looks up the dictionary and adds the
                # corresponding morse code
                # along with a space to separate
                # morse codes for different characters
                cipher += MORSE_CODE_DICT[letter] + " "
            else:
                # 1 space indicates different characters
                # and 2 indicates different words
                cipher += " "

        return cipher

    # Function to decrypt the string
    # from morse to english
    @staticmethod
    def decrypt(message):

        # extra space added at the end to access the
        # last morse code
        message += " "

        decipher = ""
        citext = ""
        for letter in message:

            # checks for space
            if letter != " ":

                # counter to keep track of space
                i = 0

                # storing morse code of a single character
                citext += letter

            # in case of space
            else:
                # if i = 1 that indicates a new character
                i += 1

                # if i = 2 that indicates a new word
                if i == 2:

                    # adding space to separate words
                    decipher += " "
                else:

                    # accessing the keys using their values (reverse of encryption)
                    decipher += list(MORSE_CODE_DICT.keys())[
                        list(MORSE_CODE_DICT.values()).index(citext)
                    ]
                    citext = ""

        return decipher

    @staticmethod
    def decode_cipher(cipher: str) -> str:
        bs64_str = cipher[:3] + cipher[4:]

        decoded_bytes = base64.b64decode(bs64_str)
        decoded_str = decoded_bytes.decode("utf-8")
        return decoded_str
