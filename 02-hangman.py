"""
Below is template code for the "Hangman" assignment. Adapt it to your needs.
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

    def show_letter(self, letter_list):
        new_word = ''
        for letter in self._secret_word:
            if letter in letter_list:
                new_word = new_word + letter.upper() + ' '
            else:
                new_word = new_word + '_' + ' '
        
        return new_word

    def check(self, letter):
        if letter in self._secret_word:
            return True
        else:
            return False

    @property
    def letters(self):
        return set(self._secret_word)

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

    def play(self):
        # Play the game!
        pass

if __name__ == "__main__":
    game = Game(10)
    game.play()