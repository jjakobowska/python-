#program wypisuje imiona kotów w klejności jaką podasz używając listy
catNames = []
while True: #pętla która dodaje imiona kotów do listy
    print('Enter the name of cat ' + str(len(catNames)+1))
    print(' Or nothing to stop.' )
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # dodaje imie do listy
print(' The cat names are:')
for name in catNames:
    print(' ' + name)
