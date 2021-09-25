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

#Functions
def banner_printer ():
    custom_fig = Figlet(font='ogre')
    print(Fore.GREEN + custom_fig.renderText('Pyth3rCrack'))
    print('Pyth3rCrack Zip File cracker v' + version)
    print('Made by Pyth3rEx')
    print('===============')
    print(Style.RESET_ALL)
    return

def wordlist_creator (wordList):
    #Wordlist naming
    print('Define a name for the wordist:')
    wordlist_name=input()
    RBAPG.setWordlistName(wordlist_name)
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
    wordList = path + wordlist_name
    os.rename(wordlist_name, wordList)
    print('Wordlist generated, ou can find it under: ' +  wordList)
    return wordList

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
    wordList = wordlist_creator(wordList)
    print(wordList)
    input()
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