# without setdefault()
spam = {'name' : 'Poka' , 'age' : 5}
if 'color' not in spam: # if there is no color in keys assign to it value black
    spam['color'] = 'black'
print(spam)

#with setdefault()
spam = {'name' : 'Poka' , 'age' : 5}
spam.setdefault('color','black')#if there is no color in keys assign to it value black
print(spam)
spam.setdefault('color','white')#if there is no color in keys assign to it value white
print(spam) #but there is 'color' key so color is still black not white
