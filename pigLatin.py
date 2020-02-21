#! python
# pig latin


import pyperclip

word = pyperclip.paste() # copied word is pasted to word variable

vowels = ['a','e','i','o','u', 'A', 'E', 'I','O','U']

if word[0] in vowels:
	word = word+'yay'

pyperclip.copy(word)

