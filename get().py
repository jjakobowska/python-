spam = {'name' : 'Zophie', 'age':7}
animal = 'cats'
print('I am ' + str(spam.get('name' , 0))) 
print('I am ' + str(spam.get('age' , 17)) + ' years old')
print('I like ' + str(spam.get('animals', animal))) #there is no animals key in a dictionary so we will use animals variable assigned previously

