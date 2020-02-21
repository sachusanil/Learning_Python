import pprint

print("Enter a sentence to count to display the count of characters")
sentence = input()
count={}
for character in sentence:
    count.setdefault(character, 0)
    count[character]=count[character]+1

pprint.pprint(count)