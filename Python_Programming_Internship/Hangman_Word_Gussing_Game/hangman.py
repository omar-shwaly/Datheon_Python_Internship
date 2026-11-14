# Importing a library to select a random word

import random
from pathlib import Path

# The class definition is named "Word"


class word:

    # Defining the constructor and providing
    # it with the appropriate parameters

    def __init__(self, filename: str):

        self.words_list = self._load_words(filename)
        self.secret_word = random.choice(self.words_list).lower()
        self.guessed_letters = set()

    # Define a private function named `load_words`
    # that takes a string representing a filename (`filename: str`)
    # as an argument and returns a list of words (`-> list`)

    def _load_words(self, filename: str) -> list:
        try:
            file_path = Path(__file__).parent / filename

            # I am preparing the file for reading.
            with open(file_path, "r", encoding="utf-8") as file:

                # First, I created an empty list to collect the words. Then,
                # I iterated through the file line by line,
                # checked that each line was not empty, cleaned the word,
                # converted it to lowercase, and added it to the list.

                words = []
                for line in file:
                    if line.strip():
                        clean_word = line.strip().lower()
                        words.append(clean_word)

                        # The function checks whether there are any words in the list
                        # If there are it returns the list after cleaning all the words it contains
                        # If not it creates a list containing some fallback words—added
                        # as a precaution—to ensure the code can still function
                if words:
                    return words
                else:
                    return ["python", "developer", "internship"]
        except FileNotFoundError:
            return ["python", "developer", "internship"]

    # This function iterates through each letter of the word guessed by the player
    # and checks whether that letter exists in the random word chosen by the computer
    # If it is present, the letter is displayed as is
    # if not, an underscore (_) is printed in its place  Additionally
    # there is a function called `join()`
    # that combines the characters stored in the list into a single string
    # ensuring they are not printed enclosed in square brackets ([]).

    def get_display_word(self) -> str:
        display_word = []

        for letter in self.secret_word:

            if letter in self.guessed_letters:
                display_word.append(letter)

            else:
                display_word.append("_")

        # Join all elements in the list into a single string separated by spaces
        return " ".join(display_word)

    def guess_letter(self, letter: str) -> bool:

        letter = letter.lower()
        self.guessed_letters.add(letter)
        return letter in self.secret_word

    # This function iterates through the letters of the word chosen by the computer
    # one by one. If any of these letters are missing from the word guessed by the player
    # it returns `false`
    # if all of them are present
    # it returns `true`

    def is_won(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False

        return True


# The class definition is named "Game"


class Game:

    # Defining the constructor and providing
    # it with the appropriate parameters

    def __init__(self, filename: str, max_attempts: int = 6):
        self.word_manager = word(filename)
        self.max_attempts = max_attempts
        self.wrong_attempts = 0

        # I created a list containing all the interactive visual elements needed for the game within the `Attribute` class
        # Then  inside the `main` function—within a loop—I accessed this list
        # referencing each item using an index that corresponds to the player's current state
        # (specifically, the number of errors made).
        self.stages = [
            """
               --------
               |      |
               |      
               |     
               |      
               |     
            ------------
            """,
            """
               --------
               |      |
               |      O
               |     
               |      
               |     
            ------------
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      
               |     
            ------------
            """,
            """
               --------
               |      |
               |      O
               |     /|
               |      
               |     
            ------------
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |      
               |     
            ------------
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     / 
               |     
            ------------
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     / \\
               |     
            ------------
            """,
        ]

    # The purpose of this function is to check whether the game has ended
    # It does this by using the object created from the 'words' class to access and call the 'win' function
    # if that function returns 'true'then the game has indeed ended Alternatively
    # if the number of errors reaches the maximum allowed limit—which is six—the game is also considered over

    def is_game_over(self) -> bool:
        has_won = self.word_manager.is_won()
        is_out_of_attempts = self.wrong_attempts >= self.max_attempts
        if has_won == True:
            return True
        elif is_out_of_attempts == True:
            return True
        else:
            return False

    # This function will perform a check using the object created from the `Word` class—specifically via the `guess_letter`
    # method—to determine whether the guessed letter is correct. If it is correct
    # the function will return `true`
    # if incorrect it will return `false`
    # and increment the error count by one.

    def play_turn(self, letter: str) -> str:

        #
        if letter in self.word_manager.guessed_letters:
            return "You already guessed that letter! Try a different one."

        is_correct = self.word_manager.guess_letter(letter)
        if is_correct == False:
            self.wrong_attempts = self.wrong_attempts + 1
            return "Incorrect! The letter is not in the word."
        else:
            return "Great! The letter is in the word."


if __name__ == "__main__":
    filename = "words.txt"

    game = Game(filename, max_attempts=6)

    print("--- Welcome to Hangman Game ---")

    while game.is_game_over() == False:

        # The items in the list are rendered using Bandbox
        # if an error occurs
        # the error code is displayed and the status is printed accordingly

        print(game.stages[game.wrong_attempts])

        # The characters entered by the user are stored in a list
        # Then the program checks whether there are any characters in that list
        # if there are it prints them using `join`
        # and if not  it prints a message indicating their absence.

        guessed_sorted = sorted(list(game.word_manager.guessed_letters))
        if guessed_sorted:
            print("Guessed letters:", " ".join(guessed_sorted))

        # else:
        # print("None")

        print("\nCurrent word:", game.word_manager.get_display_word())
        print(f"Remaining wrong attempts: {game.max_attempts - game.wrong_attempts}")

        user_letter = input("Enter a letter to guess:\n ")

        result_message = game.play_turn(user_letter)
        print(result_message)
        print("-" * 30)

    print(game.stages[game.wrong_attempts])  #
    if game.word_manager.is_won() == True:
        print(
            "\n Congratulations! You won and guessed the correct word:",
            game.word_manager.secret_word,
        )
    else:
        print(
            "\n Unfortunately, you ran out of attempts and lost! The secret word was:",
            game.word_manager.secret_word,
        )
