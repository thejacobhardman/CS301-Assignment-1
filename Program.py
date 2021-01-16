# Jacob Hardman
# John Minney
# Niko Antuna
# O Moo Gay
# Dr. Miller
# CS 301 
# First Commit: 1/12/2021
# Last Commit: 1/16/2021
# Version: 1.0

from itertools import combinations
import time, os

### EXTRA FUNCTIONS
def cls(): # I got this method to clear the console screen from StackOverflow.com: https://stackoverflow.com/a/684344 (Jacob)
    os.system('cls' if os.name=='nt' else 'clear')

def Get_Letter_Set():
    while True:
        letter_set = input('Enter a String of 6 characters: ').lower()
        if len(letter_set) == 6:
            return letter_set
        else:
            print('Only a String of 6 characters are allowed...')

def Is_Letter_In_String(letters, word):
    letter_check = [characters in letters for characters in word]
    return(all(letter_check))

# Generate the eight tiles used for Problem 6
# I actually learned this last year when I did a Google Coding competition (John)
def Generate_All_Eight_Tiles():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    all_tiles = set(combinations(alphabet, 8))
    valid_tiles = []
    for tiles in all_tiles:
        valid = Is_Letter_In_String(tiles, vowels)
        if valid:
            valid_tiles.append(tiles)
    return [''.join(tile) for tile in valid_tiles]

def Filter_Eight_Letter_Words():
    file = open("words.txt", "r")
    filtered_words_list = []
    for line in file:
        if len(line) == 10:
            word = line[:-2]
            filtered_words_list.append(word)

    file.close()
    return filtered_words_list

##################################### PROBLEMS START HERE ###########################################

#Problem 1: Sum of Integers.
def Problem_One():
    n = int(input("Enter a positive integer: "))
    total = n * (n+1) / 2
    print("The sum of the first",n,"positive integers =",total)

#Problem 2: Valid Word?
def Problem_Two():
    userWord = input('Enter a word to validate: ')
    with open('words.txt') as words_file:
        for line in words_file:
            if userWord == line.strip():
                print('{} is a valid word!\n'.format(userWord))
                return True
    print('{} is not a valid word.\n'.format(userWord))
    return False

#Problem 3: Can word be made from tiles?
def Problem_Three():
    tiles = ["b", "e", "r", "a", "t", "d", "s"] # Change this list and the word below it for different tests
    word = "darts"

    joined_tiles = ''.join(tiles)

    word_construct = ""
    used_letters = ""

    for outside_counter in range(len(word)):
        for inside_counter in range(len(tiles)):
            is_letter_valid = Is_Letter_In_String(word[outside_counter], tiles[inside_counter])

            if is_letter_valid:
                word_construct += tiles[inside_counter]
                used_letters += tiles[inside_counter]
                used_letters += tiles[inside_counter]
                tiles[inside_counter] = ""

    if word_construct == word:
        print("You can make the word '" + word + "' with the tiles '" + joined_tiles + ".'")
    else:
        print("You can NOT make the word '" + word + "' with the tiles '" + joined_tiles + ".'")

#Problem 4: Find all words that can be made from tiles.
def Problem_Four():
    wordTile = "retains"
    print(f"Given the tileset: {wordTile}, you could make the words: ")
    with open("words.txt","r") as texts:
        words = texts.read().split('\n')
    for word in words:
        if len(word) == len(wordTile) and sorted(word)==sorted(wordTile):
            print(word)
    time.sleep(1)

#Problem 5: NYT Spelling Bee Puzzle.
def Problem_Five():
    letters_of_the_day = Get_Letter_Set() # Letters from the Example
    center_letter = input('Please Enter your Center Character: ')
    letters_of_the_day += center_letter
    solved_words = []
    with open('words.txt') as words_file:
        for line in words_file:
            word = line.strip()
            if (len(word) >= 5) and (center_letter in word) and (Is_Letter_In_String(letters_of_the_day, word)):
                solved_words.append(word)
    if (len(solved_words) != 0):
        print('\nFound Words:')
        print(*solved_words, sep=', ')
    else:
        print('Words not found...')

#Problem 6: Most bingos?
# def Problem_Six():
#     # The way I'm doing this it is going to run slow... but I can't think of anything else (John)
#     print('Loading... No seriously this takes FOREVER...')
#     tile_sets = Generate_All_Eight_Tiles()
#     best_bingo = ([], 0)
#     all_words = [line.strip() for line in open('words.txt').readlines()]
#     for tile_set in tile_sets:
#         bingo = 0
#         for word in all_words:
#             if (len(word) == 8) and (Is_Letter_In_String(tile_set, word)):
#                 bingo += 1
#         if (bingo > best_bingo[1]):
#             best_bingo = (tile_set, bingo)
#     print('The Best Bingo is: ' + best_bingo)

def Problem_Six():
    # The way I'm doing this it is going to run slow... but I can't think of anything else (John)
    print('Loading... No seriously this takes FOREVER...')
    tile_sets = Generate_All_Eight_Tiles()
    print(tile_sets)
    best_bingo = ([], 0)
    filtered_word_list = Filter_Eight_Letter_Words()
    #all_words = [line.strip() for line in open('words.txt').readlines()]
    for tile_set in tile_sets:
        bingo = 0
        for word in filtered_word_list:
            if (Is_Letter_In_String(tile_set, word)):
                bingo += 1
        if (bingo > best_bingo[1]):
            best_bingo = (tile_set, bingo)
    best_bingo_string = best_bingo[0]
    print(f"The Best Bingo is: {best_bingo_string}")

def Reset():
    input("Press any key to continue.")
    cls()

def Main():
    isRunning = True
    while isRunning:
        print("Welcome!")
        print("\n1: Sum of Integers"
            + "\n2: Valid Word?"
            + "\n3: Can word be made from tiles?"
            + "\n4: Find all words that can be made from tiles."
            + "\n5: NYT Spelling Bee Puzzle."
            + "\n6: Most bingos?"
            + "\n7: Exit Program.")
        selection = input("\nPlease enter the corresponding number for the program that you'd like to test: ")

        if int(selection) == 1:
            Problem_One()
        elif int(selection) == 2:
            Problem_Two()
        elif int(selection) == 3:
            Problem_Three()
        elif int(selection) == 4:
            Problem_Four()
        elif int(selection) == 5:
            Problem_Five()
        elif int(selection) == 6:
            Problem_Six()
        elif int(selection) == 7:
            isRunning = False
        else:
            print("Please enter a valid selection.")

        Reset()

Main()
