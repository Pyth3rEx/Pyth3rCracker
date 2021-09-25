#Base Imports
import os
import re
from colorama.initialise import reset_all
from pyfiglet import Figlet
from colorama import init
init()
from colorama import Fore, Back, Style

#Addon Imports
import zipfile
import tqdm
from tqdm import tqdm
import RBAPG
RBAPG=RBAPG.RuleBasedAttackPasswordGenerator()

#Vars
version = '0.01'
#Variables
wordList = 'None'
path = 'None'
numBool = True
uAlBool = True
lAlBool = True
charArray = []
password = []
i = 0
#Arrays
numeral = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
uppercaseAlpha = ['a', 'b' , 'c' , 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lowercaseAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#Functions
def banner_printer ():
    custom_fig = Figlet(font='ogre')
    print(Fore.GREEN + custom_fig.renderText('Pyth3rCrack'))
    print('Pyth3rCrack Zip File cracker v' + version)
    print('Made by Pyth3rEx')
    print('===============')
    print(Style.RESET_ALL)
    return

def wordlist_creator(wordList):
    #Wordlist naming
    print('Define a name for the wordist:')
    wordlistName=input()
    RBAPG.setWordlistName(wordlistName)
    #Password Size
    print('Set a level for combination:min 2 - max 5:')
    length=int(input())
    if length>5 or length<2:
        print("Max 5 Min 2")
        print(Fore.RED + 'ERROR 0002')
        print('exiting...')
        input()
        exit(1)
    RBAPG.setLengthOfGeneratedPassword(int(length))
    #Targets
    print('Define target words: (separated by a space)')
    words = input()
    RBAPG.wordlist = words
    #Generation
    RBAPG.generate_wordlist()
    os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal
    path = 'wordlists\\'
    wordList = path + wordlistName
    os.rename(wordlistName, wordList)
    print('Wordlist generated, you can find it under: ' +  wordList)
    return wordList

def brutelist_creator(numBool, uAlBool, lAlBool, minLen, maxLen, charArray, wordlistName):
    i = 0
    #Setup character array
    if uAlBool == True:
        charArray = charArray + uppercaseAlpha
    if lAlBool == True:
        charArray = charArray + lowercaseAlpha
    if numBool == True:
        charArray = charArray + numeral

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
    return

def printer(password):
    with open(wordlistName, 'a') as f:
        print(str(password) + '\n')
        f.write(str(password) + '\n')
        return

#Start of UI
os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal
banner_printer()
path = 'zipFiles\\shitty_encrypted_files_go_here\\'
print('Name of Zip file in the \'shitty_encrypted_files_go_here\' folder:')
zip_file = path + input()
zip_file = zipfile.ZipFile(zip_file)
print('Do you have a wordlist? If not we\'ll create one together ;) (Y/N)')
answer = input()
if answer == 'N':
    print('What would you like to create? (Worlist = W / Brutelist = B)')
    answer = input()
    if answer == 'W':
        wordList = wordlist_creator(wordList)
        print(wordList)
        input()
    elif answer == 'B':
        os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal
        print('Please chose a name for your wordlist:')
        wordlistName = input()
        while True:
            os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal
            print('Please chose your charSet:')
            print('[1] - Numeric         : ' + str(numBool))
            print('[2] - Lowercase Alpha : ' + str(uAlBool))
            print('[3] - Uppercase Alpha : ' + str(lAlBool))
            print('Correct? (Y/°)')
            answer = input()
            if answer == 'Y':
                break
            else:
                if answer == '1':
                    numBool = not numBool
                elif answer == '2':
                    uAlBool = not uAlBool
                elif answer == '3':
                    lAlBool = not lAlBool
        os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal
        print('Enter the minimum password length:')
        minLen = int(input())
        print('Enter the maximum password length:')
        maxLen = int(input())
        brutelist_creator(numBool, uAlBool, lAlBool, minLen, maxLen, charArray, wordlistName)
        path = 'wordlists\\'
        wordList = path + wordlistName
        os.rename(wordlistName, wordList)
        print('Wordlist generated, you can find it under: ' +  wordList)
    else:
        print(Fore.RED + 'ERROR 0003')
        print('exiting...')
        input()
        exit(1)
elif answer == 'Y':
    path = 'wordlists\\'
    print('Name of the wordlist:')
    wordList = path + input()
else:
    print(Fore.RED + 'ERROR 0001')
    print('exiting...')
    input()
    exit(1)

#cracker
nWords = len(list(open(wordList, "rb")))
print('Ready to test \'' + str(nWords) + '\' passwords.')
input()
print('Testing...')

with open(wordList, "rb") as wordList:
    for i in tqdm(wordList, total=nWords, unit='passwords'):
        try:
            zip_file.extractall(pwd=i.strip())
        except:
            continue
        else:
            print('[+] Password found:', i.decode().strip())
            exit(0)
print("[!] Password not found, update wordlist.")