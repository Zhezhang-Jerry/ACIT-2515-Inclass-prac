"""
Below is template code for the "Hangman" assignment. Adapt it to your needs.
"""

NUMBER_OF_TURNS = 10

class SecretWord:
    """
    Represents a word to be guessed by the player
    """
    def __init__(self):
        # Open the file and set the _secret_word
        pass

    @property
    def letters(self):
        # Return a collection of unique letters in the word
        pass

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