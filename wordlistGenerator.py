#Password rules:
#======
# ZipCrypto:
# 1-80 char
# alphanumeric
# no special character
# case sensitive
#======
# AES-256
# 1-32char (128 bit encryption)
# 1-64char (256 bit encryption)
# alphanumeric
# no special character
# case sensitive

#Arrays
numeral = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
uppercaseAlpha = ['a', 'b' , 'c' , 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lowercaseAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Start
#Variables
minLen = 2
maxLen = 4
uAlBool = True
lAlBool = True
numBool = True
charArray = []
password = []
i = 0

#Setup character array
if uAlBool == True:
    charArray = charArray + uppercaseAlpha
if lAlBool == True:
    charArray = charArray + lowercaseAlpha
if numBool == True:
    charArray = charArray + numeral

#=============

### ARC's pseudocode:
# password = charArray[0] * minLen
# while (max length not reached)
#   if (last character is Z)
#     find all Z's at the end and replace them with A's # (like going from 199 to 200)
#     if the pw was all Z's
#       insert A at the beginning
#     else
#       increment the letter immediately before the last Z
#   else
#     increment last character
#   print pw

def printer(password):
    with open('reception.txt', 'a') as f:
        print(str(password) + '\n')
        f.write(str(password) + '\n')
        return

#Create the minimum password
while i < minLen:
    password.append(charArray[0])
    i = i + 1
    
allZ = True #Reset allZ
while i <= maxLen: #While max lenght not reached
    printer(password)
    if password[-1] == charArray[-1]: #If last char of the password match last char of the charArray (start incrementing above)
        for a in reversed(range(len(password))): #For all letters in the password (check if last hit)
            if password[a] == charArray[-1]: #if letter [a] of the password is the last available letter
                allZ = True #Maxed out?
                password[a] = charArray[0] #set that letter to the first possibility
            else: #otherwise exit for loop 'For all letters in the password (check if last hit)'
                allZ = False #The password is not maxed out yet
                password[a] = charArray[charArray.index(password[a])+1] #Increment letter just before the first last character (yea I know this dosn't make sense screz you :P)
                break #GTFO
        if allZ == True: #If all letters are the last possible char (+1 number of letters)
            password.insert(0, charArray[0]) #add the first possible char in first possition
            i = i + 1 #add 1 to the lengh of the word
    else: #If the last character is not maxed out...
        password[-1] = charArray[charArray.index(password[-1])+1] #Increment last char