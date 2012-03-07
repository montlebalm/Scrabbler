import config
from words import Words

def is_key(key):
	return key in Words.hashed

def is_word(word):
	return word in Words.words

def get_words(key):
	return Words.hashed[key]

def get_letter_value(letter):
	return config.letters[letter].value