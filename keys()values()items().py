#values() keys() and items()

spam = {'color' : 'red', 'age' :42}

for v in spam.values():
    print(v) #output : 'red', 42
    
for k in spam.keys():
    print(k) #output : 'color' , 'age'
    
for i in spam.items():
    print(i) #output : ('color' , 'red') ('age' , 42)
    
#tworzenie listy z np keys()
spam.keys()
print(list(spam.keys()))

#using multiple assignment
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
