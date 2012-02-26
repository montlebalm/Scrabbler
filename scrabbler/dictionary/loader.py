import config
from words import Words

def load():
    """Run through a list of hashed and create a sorted string from each
    word's letters. Assign the sorted string as a key for all hashed that
    share the same letters."""
    for line in open(config.filepath, 'r'):
        line = line.strip()
        line_sorted = ''.join(sorted(line))

        if line_sorted not in Words.hashed:
            Words.hashed[line_sorted] = []

        # Store the real hashed as a list
        # We need line_sorted as the key for fast lookup later
        Words.hashed[line_sorted].append(line)

        # Also add the word to a standard list
        # We'll use this to quickly determine wordiness later
        Words.words.append(line)