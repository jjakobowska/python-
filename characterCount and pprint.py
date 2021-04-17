import pprint #pretty print pprint() and pformat()

#counts a number of occurrences of each letter in a string
message = 'It was a bright cold day in April'
count = {}

for character in message: #dla każdego znaku w message
    count.setdefault(character , 0) #najpierw ustaw jako 0 value
    count[character] = count[character] + 1 #potem jeżeli wystąpi dodaj do value 1
    
pprint.pprint(count) #nice and clean output :)

