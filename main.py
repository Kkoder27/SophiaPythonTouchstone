"""This is a snippet of python code that serves to satisfy the touchstone requirements of
CS1100 (Intro to python) from Sophia Learning LLC."""
# See https://github.com/Kkoder27/SophiaPythonTouchstone for more information

def caesarSolve():
    caesarInput = input('Input encrypted string to be solved')
    encryptedSnapshot = list(caesarInput)
    encodedLetterCase = []
    for letter in encryptedSnapshot:
        if ord(letter)>=65 and ord(letter)<=90:
            encodedLetterCase.append(True)
        elif ord(letter)>=97 and ord(letter)<=122:
            encodedLetterCase.append(False)
        else: encodedLetterCase.append(letter)
    print(encryptedSnapshot)
    print(encodedLetterCase)
    return
caesarSolve()