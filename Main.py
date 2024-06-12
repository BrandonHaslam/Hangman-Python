import test
import random
import hangman_words
import hangman_art

class Hangman:
  def __init__(self, words, hangman_art):
    self.art = hangman_art
    self.words = words
    self.total_words = len(words)
    self.game_word = ''
    self.player_word = ''
    self.lives = len(self.art.stages)
    self.stage = self.art.stages[self.lives - 1]
    self.guesses = []
    self.reset_game_state()

  def reset_game_state(self):
    self.game_word = self.words[random.randint(0, self.total_words - 1)].lower()
    self.player_word = '_' * len(self.game_word)
    self.lives = len(self.art.stages)
    self.guesses = []
    print(self.game_word)
    print(self.player_word)
  
  def guess_letter(self):
    guess = input('Choose a letter\n').lower()
    if len(guess) > 1:
      print('Invalid input! Only enter one letter.')
    if guess in self.guesses:
      print('You have already chosen that letter.')
      return
    if self.check_game_word(guess) == True:
      print(self.guesses)
      print(self.player_word)
      return
    else:
      # Add lose life logic
      self.lose_life()
      return

  def check_game_word(self, input_letter):
      updated_player_word = list(self.player_word)  # Convert game_word to a list for mutability
      letter_exists = False  # Initialize flag to check if letter exists

      for index, letter in enumerate(self.game_word):  # Loop through the current_word
          if letter == input_letter:
              letter_exists = True
              updated_player_word[index] = input_letter  # Update the game word with the correct letter

      self.player_word = ''.join(updated_player_word)  # Convert list back to string
      self.guesses.append(input_letter)
      return letter_exists  # Return whether the letter was found

  def lose_life(self):
    self.lives -= 1
    self.stage = self.art.stages[self.lives]
    print(self.stage)
    print(self.guesses)
    print(self.player_word)

  def run_game(self):
    game_active = True
    while game_active == True:
      self.guess_letter()
      if(self.player_word == self.game_word):
        print(f'Congratulations you guessed the word - {self.game_word}!')
        game_active = False
      if(self.lives == 0):
        print(f'You Lose! The word was {self.game_word}.')
        game_active = False
game = Hangman(hangman_words.word_list, hangman_art)
game.run_game()
# To Do
# Add real life system