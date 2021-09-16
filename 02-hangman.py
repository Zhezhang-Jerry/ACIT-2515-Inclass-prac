"""
program: 02-hangman.py
Author: Zhe Zhang A01257572 Set B
Date: Sep 14 2021
"""

from hashlib import new
import random

NUMBER_OF_TURNS = 10

class SecretWord:
    """
    Represents a word to be guessed by the player
    """
    def __init__(self):
        self._secret_word = None
        if self._secret_word == None:
            with open ('words.txt', 'r') as f:
                content = f.readlines()
                word_list = [i.strip() for i in content]

            self._secret_word = word_list[random.randint(0, len(word_list) - 1)]
            print(self._secret_word)

    def show_letter(self, letter_list):
        new_word = ''
        for letter in self._secret_word:
            if letter in letter_list:
                new_word = new_word + letter.upper() + ' '
            else:
                new_word = new_word + '_' + ' '
        
        return new_word

    def check(self, new_word):
        if new_word == self._secret_word:
            return True
        else:
            return False

    @property
    def letters(self):
        return set([letter.upper() for letter in self._secret_word])

class Game:
    """
    Represents a game being played (multiple turns)
    """
    def __init__(self, turns):
        """
        Sets the initial attributes
        """
        self.word = SecretWord()
        self.turns_remaining = turns
        self.letters = []

    def play_one_round(self):
        player_input = input("Please enter the letter you guess: ")
        guess = ""
        if player_input.isalpha() is True:
            if player_input.lower() != "check":
                guess = player_input
                self.letters.append(guess.lower())
                new_word = self.word.show_letter(self.letters)
                print(new_word)
            else:
                final_guess = input("Please guess the word: ")
                return self.word.check(final_guess)
        else:
            player_input = input("Please enter a letter or type the word check, try again: ")


    def play(self):
        result = False
        while result is not True:
            if self.turns_remaining != 0:
                print("you have",self.turns_remaining, "times remaining")
                self.turns_remaining = self.turns_remaining - 1
                result = self.play_one_round()
            else:
                print("Sorry, you lose.")

        print("Yeah, you win the game!")

        

if __name__ == "__main__":
    game = Game(10)
    game.play()