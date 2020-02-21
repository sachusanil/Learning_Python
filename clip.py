#! python3
# clip.py - A multi Clipboard programme

text = {'agree':"""Yes, I agree. That sounds fine""", 
		'busy': """ Sorry, can we do this later or next week?""", 
		'upsell':"""Would you consider making this a monthly donation"""}

import sys
import pyperclip

if len(sys.argv) < 2:
	print('Usage: python3 clip.py [keyphrase] - copy phrase text')
	sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
	pyperclip.copy(text[keyphrase])
	print('Text copied')
else:
	print(f('There is no text for {keyphrase}'))