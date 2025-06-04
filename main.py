"""This is a snippet of python code that serves to satisfy the touchstone requirements of
CS1100 (Intro to python) from Sophia Learning LLC."""
# See https://github.com/Kkoder27/SophiaPythonTouchstone for more information

import math
from english_words import get_english_words_set as gew #provides set of bulk english words
englishSet = gew(['web2'], lower=True)

def encodeCaseInfo(caesarInput):
    encryptedSnapshot = list(caesarInput) #string to list will be used to work with ASCII information

    encodedLetterCase = [] #this block will be used in the case of a mixture of upper and lower case values in order to retain case information
    for letter in encryptedSnapshot:
        if ord(letter)>=65 and ord(letter)<=90:
            encodedLetterCase.append(True)
        elif ord(letter)>=97 and ord(letter)<=122:
            encodedLetterCase.append(False)
        else: encodedLetterCase.append(letter) #maintains current symbol if not english alphabet, use to catch errors later
    return encodedLetterCase

def loopCaesarValues(shiftValue, digit): #input letter & shift value, output new letter
    while shiftValue>25:
        shiftValue-=26
    output = digit + shiftValue
    if output>122:
        output = output-26
    return output

def bruteForceShift(caesarInput): #takes string, and turns into list of strings for each caeser shift
    testList = []
    for item in list(caesarInput.lower()): #list of letters to list of ASCII numerals
        testList.append(ord(item))
    outputArr = []
    for num in range(26):
        tempList = []
        shiftValue = num
        step = 0
        for digit in testList:
            if digit>=97 and digit<=122:
                tempList.append(chr(loopCaesarValues(shiftValue, digit)))
            else: tempList.append(chr(testList[step]))
            step+=1
        outputArr.append(tempList)
    for arr in range(len(outputArr)):
        outputArr[arr] = ''.join(outputArr[arr])
    return outputArr

def cutNonAlphas(string): #cuts out nonalphabeticals for english comparison
    expandedList = list(string)
    step=0
    outputString = ''
    for item in expandedList:
        if ord(item)>=97 and ord(item)<=122 or ord(item)==32: #catches lowercase letters or a space
            outputString = outputString + expandedList[step]
        step+=1
    #print(outputString)
    return outputString

def englishComparison(manyList):
    probabilityList = []
    for cipherOption in manyList:
        accurateWords = 0
        cipherWords = cutNonAlphas(cipherOption).split(' ')
        print(cipherWords)
        for word in cipherWords:
            if word in englishSet:
                accurateWords+=1
        probability = math.trunc((accurateWords/len(cipherWords))*100)
        probabilityList.append(probability)
    cipherNum, steps, maxProb = 0,0,0
    for probability in probabilityList:
        if probability > maxProb:
            maxProb = probability
            cipherNum = steps
        steps+=1
        #print([cipherNum, maxProb])
    #print(probabilityList)
    return cipherNum
    
def caesarSolve():
    caesarInput = input('Input encrypted string to be solved')
    encodedLetterCase = encodeCaseInfo(caesarInput) #encoded information about case of letters
    manyList = bruteForceShift(caesarInput) #list of strings corresponding to each possible caeser shift
    cipherNum = englishComparison(manyList)
    #print(manyList[cipherNum])
    #print(encodedLetterCase)
    #print(manyList)
    return manyList[cipherNum]
caesarSolve()