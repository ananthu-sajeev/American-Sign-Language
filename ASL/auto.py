from autocorrect import Speller

# Initialize the Speller object
spell = Speller()

# Test word
misspelled_word = "watermeyqlom"

# Get the corrected word
corrected_word = spell(misspelled_word)

print(f"Original word: {misspelled_word}")
print(f"Corrected word: {corrected_word}")
