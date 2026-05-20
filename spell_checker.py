import difflib
import os


class TamilSpellChecker:
    def __init__(self, dictionary_path):
        """Initializes the spell checker and loads the dictionary."""
        self.dictionary = set()
        self.load_words(dictionary_path)

    def load_words(self, path):
        """Loads Tamil words from a text file into a set for fast lookup."""
        if not os.path.exists(path):
            print(f"Error: Dictionary file not found at {path}")
            return

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                if word:
                    self.dictionary.add(word)
        print(f"Loaded {len(self.dictionary)} words into the dictionary.")

    def check_word(self, word):
        """Returns True if the word is in the dictionary."""
        return word in self.dictionary

    def suggest_corrections(self, word, num_suggestions=3):
        """Suggests corrections for a misspelled word."""
        if self.check_word(word):
            return f"✅ '{word}' is spelled correctly."

        # cutoff=0.6 means the suggestion must be at least 60% similar to the target word
        closest_matches = difflib.get_close_matches(word, self.dictionary, n=num_suggestions, cutoff=0.6)

        if closest_matches:
            suggestions = ", ".join(closest_matches)
            return f"❌ '{word}' is misspelled. Did you mean: {suggestions}?"
        else:
            return f"❌ '{word}' is misspelled. No close suggestions found in the dictionary."


if __name__ == "__main__":
    # Define the path to the dictionary file
    dict_path = os.path.join("data", "tamil_words.txt")

    # Initialize the spell checker
    checker = TamilSpellChecker(dict_path)

    print("-" * 40)

    # Test Case 1: Correct word
    test_word_1 = "வணக்கம்"
    print(checker.suggest_corrections(test_word_1))

    # Test Case 2: Misspelled word (வனக்கம் instead of வணக்கம்)
    test_word_2 = "வனக்கம்"
    print(checker.suggest_corrections(test_word_2))

    # Test Case 3: Completely unknown word
    test_word_3 = "கணினி"
    print(checker.suggest_corrections(test_word_3))

    print("-" * 40)